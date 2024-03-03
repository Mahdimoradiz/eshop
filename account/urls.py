from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path('profile', views.Profile.as_view(), name="profile"),
    path('login', views.login_form_view, name="login_form"),
    path('register', views.register_form_view, name="register_form"),
]
