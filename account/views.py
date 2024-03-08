from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from django.views import View
from account.forms import LoginForm, OtpLoginForm, CheckOtpForm
import ghasedakpack
from random import randint
from django.utils.crypto import get_random_string
from account.models import Otp, User

SMS = ghasedakpack.Ghasedak("428e2ff4e66399c604d698a366ce9d752428c2aad134471334cdff85e6721862")

class UserLoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "account/login.html", {'form': form})
    
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error("username", "invalid number")
        else:
            form.add_error("username", "invalid number")
            
        return render(request, "account/login.html", {'form': form})
     
           
class UserRegisterView(View):
    def get(self, request):
        form = OtpLoginForm()
        return render(request, "account/register.html", {'form': form})
    
    def post(self, request):
        form = OtpLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            randcode = randint(1000, 9999)
            print(randcode)
            SMS.verification({'receptor': cd["phone"],'type': '1','template': 'rancode','param1': {randcode}})
            token = get_random_string(length=100)
            Otp.objects.create(phone=cd["phone"], code=randcode)
            return redirect(reverse('account:check_otp') + f'?phone={token}')
        else:
            form.add_error("phone", "invalid data")
        return render(request, "account/register.html", {'form': form})
    

class CheckOtpView(View):
    def get(self, request):
        form = CheckOtpForm()
        return render(request, "account/otp_code.html", {'form': form})
    
    def post(self, request):
        token = request.GET.get('token')
        form = CheckOtpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if Otp.objects.filter(code=cd['code'], token=token).exists():
                otp = Otp.objects.get(token=token)
                user, is_create = User.objects.get_or_create(phone=otp.phone)
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                otp.delete()
                return redirect('/')
        else:
            form.add_error("code", "invalid data")
        return render(request, "account/otp_code.html", {'form': form})
    


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')