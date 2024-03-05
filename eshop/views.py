from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import TemplateView
from django.views import View



def home(request):
    return render(request, 'main/home.html')


# here writng testing view


        