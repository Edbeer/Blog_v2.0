from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'full-width'}))
    email = forms.EmailField(max_length=150, widget=forms.EmailInput(attrs={'class': 'full-width'}))
    password1 = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={'class': 'full-width'}))
    password2 = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={'class': 'full-width'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'full-width'}))
    password = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={'class': 'full-width'}))
