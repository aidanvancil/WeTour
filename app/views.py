from django.shortcuts import render, redirect, reverse
from app.forms import UserFormCreation
from app.models import TourGuide, User, Trip
from django.contrib.auth.decorators import login_required
import environ

env = environ.Env()
environ.Env.read_env()


def landing_page(request):
    context = {'background_color': '#000000'}
    return render(request, 'landing_page.html', context)

def signup(request):
    if request.method == 'POST':
        f = UserFormCreation(request.POST)
        if f.is_valid():
            f.save()
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

def homepage(request):
    return render(request, 'homepage.html')

def profile(request):
    return render(request, 'profile.html')

def payments(request):
    return render(request, 'payments.html')

def trip(request):
    return render(request, 'trip.html')

def tourguide(request):
    return render(request, 'tourguide.html')

