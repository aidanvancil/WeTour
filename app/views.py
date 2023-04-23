from django.shortcuts import render, redirect, reverse
from app.forms import UserFormCreation, TripForm, GuideForm, ProfileRegisterForm
from app.models import TourGuide, Trip, User, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import login as log
from django.contrib.auth import logout as auth_logout
import os
from twilio.rest import Client
import environ
import cohere

co = cohere.Client('<CH11rgIb6Qn54wJphehBGeMm0EHmuJJxBXiS3IAS>')
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
    'Deutsch',
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
    auth_logout(request)
    return redirect('login')

@login_required(login_url='login')
def homepage(request):
    trips = Trip.objects.filter(user=request.user).all()
    trips_count = Trip.objects.filter(user=request.user).count()
    context = {'homepage_T': True, 'trips':trips, 'trips_count':trips_count}
    return render(request, 'homepage.html', context)

@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html', {'no_footer': True, 'profile_T': True})

@login_required(login_url='login')
def about_us(request):
    return render(request, 'aboutus.html', {'no_footer': True, 'about_T': True})

@login_required(login_url='login')
def payments(request):
    return render(request, 'payments.html', {'payments_T': True})

@login_required(login_url='login')
def view_guide(request):
    if request.method == 'GET':
        profile = spawn_trips(request)
        filtered_guides = TourGuide.objects.filter(user__state=profile[0].state)
        context = {'guides': filtered_guides, 'qualities': QUALITIES_CHOICES, 'languages': LANGUAGES}
        return render(request, 'render_guides.html', context)
    else:
        return redirect('home')

@login_required(login_url='login')
def trip(request, param=None):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            state = form.cleaned_data['state']
            city = form.cleaned_data['city']
            newTrip = Trip()
            newTrip.destination = city + ', ' + state
            newTrip.user = request.user
            newTrip.generate_map_image()
            newTrip.save()
            message = client.messages.create(
                body="""Hey! This is WeTour, thanks for booking a trip. We will reach out shortly. In the meantime, enjoy the ride.""",
                from_="+18552256052",
                to="+16616078687"
            )
            return redirect('home')
    else:
        if param is not None:
            return trip_detail_view(request, param)
        else:
            form = TripForm()
            return render(request, 'trip.html', {'form': form, 'no_footer': True, 'qualities': QUALITIES_CHOICES, 'languages': LANGUAGES})

def trip_detail_view(request, pk):
    trip_t = Trip.objects.get(pk=pk)
    return render(request, 'trip_detail.html', {'trip': trip_t})

@login_required(login_url='login')
def guide(request):
    if request.method == 'POST':
        form = GuideForm(request.POST)
        if form.is_valid():
            bio = form.cleaned_data['bio']
            profile = spawn_trips(request)
            #guide = TourGuide()
            #response = co.summarize(text=bio)
            #guide.user = profile[0]
            
            #guide.bio = response.classifications.prediction
            guide.save()
            return view_guide(request)
    else:
        form = GuideForm()
    return render(request, 'guide.html', {'form': form, 'no_footer': True, 'guide_T': True, 'qualities': QUALITIES_CHOICES, 'languages': LANGUAGES})

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