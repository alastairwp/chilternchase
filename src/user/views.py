

# Create your views here.

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django import forms
from user.models import User


class RegisterForm(UserCreationForm):
    firstname = forms.CharField()
    surname = forms.CharField()
    email = forms.EmailField()
    password1 = forms.PasswordInput
    password2 = forms.PasswordInput

    class Meta:
        model = User
        fields = ('email', 'firstname', 'surname')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['firstname'].widget.attrs.update({'class': 'form-control'})
        self.fields['surname'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})



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
            login(request, user)
            return redirect('/members/dashboard')
    else:
        form = RegisterForm()
    return render(request, 'app/signup.html', {'form': form})