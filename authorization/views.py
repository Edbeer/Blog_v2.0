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
    pass


def user_logout(request):
    pass
