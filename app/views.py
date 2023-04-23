from django.shortcuts import render, redirect, reverse
from app.forms import UserFormCreation, TripForm, GuideForm, ProfileRegisterForm
from app.models import TourGuide, Trip, User, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from django.contrib import messages
from django.contrib.auth import login as log
import os
from twilio.rest import Client
import environ

env = environ.Env()
environ.Env.read_env()

auth_token = env('AUTH_TOKEN')

QUALITIES_CHOICES = [
        'Shy',
        'Introvert',
        'Extrovert',
        'Adventurous',
        'Daring',
        'Calm',
        'Nervous',
        'Cautious',
        'Open Minded',
]

LANGUAGES = [
    'English',
    'Deutsh',
    'French',
    'Mandarin',
    'Spanish',
    'Arabic',
    'Hindi',
    'Bengali',
    'Russian',
    'Other',
]


account_sid = "AC4b86583693a11577de644ae6b6dd2b5b"
client = Client(account_sid, auth_token)
#message = client.messages.create(
 # body="Hello",
  #from_="+18552256052",
  #to="+16616078687"
#)

def spawn_trips(request):
    return (Profile.objects.filter(user=request.user))

def landing_page(request):
    context = {'background_color': '#000000'}
    return render(request, 'landing_page.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserFormCreation(request.POST)
        p_reg_form = ProfileRegisterForm(request.POST)
        if form.is_valid() and p_reg_form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            p_reg_form = ProfileRegisterForm(request.POST, instance=user.profile)
            print(p_reg_form)
            
            p_reg_form.full_clean()
            p_reg_form.save()
            messages.success(request, f'Your account has been sent for approval!')
            return redirect('login')
    else:
        form = UserFormCreation()
        p_reg_form = ProfileRegisterForm()
    context = {
        'form': form,
        'p_reg_form': p_reg_form
    }
    return render(request, 'signup.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:    
            log(request, user)
            return redirect('home')
        else:
            error_message = "Username or password is incorrect."
            context = {'error_message': error_message}
            return render(request, 'login.html', context)
    return render(request, 'login.html')

@login_required(login_url='login')
def logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def homepage(request):
    return render(request, 'homepage.html', {'homepage_T': True})

@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html', {'no_footer': True, 'profile_T': True})

def about_us(request):
    return render(request, 'aboutus.html', {'no_footer': True, 'profile_T': True})

@login_required(login_url='login')
def payments(request):
    return render(request, 'payments.html', {'payments_T': True})

@login_required(login_url='login')
def view_guide(request):
    if request.method == 'GET':
        profile = spawn_trips(request)
        filtered_guides = TourGuide.objects.filter(user__state=profile[0].state)
        context = {'guides': filtered_guides}
        return render(request, 'render_guides.html', context)
    else:
        return redirect('home')

@login_required(login_url='login')
def trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            gender = form.cleaned_data['gender']
            state = form.cleaned_data['state']
            city = form.cleaned_data['city']
            request.user.city = city
            request.user.state = state
            request.user.gender = gender

            request.user.save()
            return redirect('render_guides')
    else:
        form = TripForm()
    return render(request, 'trip.html', {'form': form, 'no_footer': True, 'qualities': QUALITIES_CHOICES, 'languages': LANGUAGES})

@login_required(login_url='login')
def guide(request):
    if request.method == 'POST':
        form = GuideForm(request.POST)
        if form.is_valid():
            gender = form.cleaned_data['gender']
            state = form.cleaned_data['state']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            # Do something with the data
            return redirect('home')
    else:
        form = GuideForm()
    return render(request, 'guide.html', {'form': form, 'no_footer': True, 'guide_T': True})

@login_required(login_url='login')
def update_profile(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        fullname = request.POST.get('full_name')
        fullname = fullname.split(' ')
        phone_number = request.POST.get('phone_number')
        user.firstname = fullname[0]
        user.lastname = fullname[1]
        user.phone_number = phone_number
        user.save()
    return render(request, 'profile.html')

def card(request):
    pass