from django import forms
from account.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from account.admin import *


class UserLoginForm(forms.ModelForm):
    username = forms.CharField(max_length=65, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'id': 'typeEmailX-2'}))
    password = forms.CharField(max_length=65, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))
    
    class Meta:
        model = User
        fields = ["username",]


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
            label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["email", "username"]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["email", "username", "password", "is_active", "is_admin"]