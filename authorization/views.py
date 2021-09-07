from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import *


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'GOOD')
            return redirect('home')
        else:
            messages.error(request, 'BAD')
    else:
        form = UserRegisterForm()
    return render(request, 'authorization/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'authorization/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')