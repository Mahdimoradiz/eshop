from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.

class Profile(View):
      def get(self, request,*args, **kwargs):
            return HttpResponse('Hello world')


def login_form_view(request):
      return render(request, "account/login.html")


def register_form_view(request):
      return render(request, "account/register.html")