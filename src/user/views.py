

# Create your views here.

from django.contrib.auth import login as cclogin, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import auth
from django.contrib import messages
from django.urls import reverse
from django import forms
from user.models import User


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user:
            if user.is_active:
                auth.login(request, user)
                return redirect(reverse('dashboard'))

            else:
                messages.warning(request,
                                 "Your account is not active. If you've just registered check your inbox for an activation email. Alternatively contact support.")
                return redirect(reverse('login'))

        else:
            messages.error(request, 'Invalid username/password')
            return redirect(reverse('login'))
    else:
        return render(request, 'app/login.html')


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            firstname = form.cleaned_data.get('firstname')
            surname = form.cleaned_data.get('surname')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=raw_password)
            cclogin(request, user)
            return redirect('/members/dashboard')
    else:
        form = RegisterForm()
    return render(request, 'app/signup.html', {'form': form})

