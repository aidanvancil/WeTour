from django.shortcuts import render, redirect, reverse
from app.forms import UserFormCreation
import environ

env = environ.Env()
environ.Env.read_env()


def landing_page(request):
    return render(request, 'landing_page.html')

def signup(request):
    if request.method == 'POST':
        f = UserFormCreation(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')

    else:
        f = UserFormCreation()
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        f = UserFormCreation(request.POST)
        if f.is_valid():
            f.save()
            return redirect('home.html')
    else:
        f = UserFormCreation()
    return render(request, 'login.html')


