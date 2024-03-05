from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


class Profile(View):
      def get(self, request,*args, **kwargs):
            return HttpResponse('Hello world')


def login_form_view(request):
      form = forms.UserLoginForm()
      message = ''
      if request.method == 'POST':
            form = forms.UserLoginForm(request.POST)
            if form.is_valid():
                  user = authenticate(
                        username = form.cleaned_data['username'],
                        password = form.cleaned_data['password'],
                  )
                  if user is not None:
                        login(request, user)
                        message = 'Hello {user.username}! You have been logged in'
                  else:
                        message = 'Login failed!'
      context = {
            'form': form,
            'message': message,
      }
      return render(request, "account/login.html", context)


@login_required
def logout_View(request):
      logout(request)
      return redirect('/')

def register_form_view(request):
      return render(request, "account/register.html")