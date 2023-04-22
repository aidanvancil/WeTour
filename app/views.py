from django.shortcuts import render, redirect, reverse
from app.forms import UserFormCreation, TripForm, GuideForm
from app.models import TourGuide, User, Trip
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import stripe
import environ

env = environ.Env()
environ.Env.read_env()

stripe.api_key = env('STRIPE_API_KEY')

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
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect('home')
        else:
            error_message = "Username or password is incorrect."
            context = {'error_message': error_message}
            return render(request, 'login.html', context)
    return render(request, 'login.html')

@login_required(login_url='login')
def logout(request):
    logout(request)
    return redirect('login')

def homepage(request):
    return render(request, 'homepage.html', {'homepage_T': True})

def profile(request):
    return render(request, 'profile.html', {'no_footer': True, 'profile_T': True})

@login_required(login_url='login')
def payments(request):
    return render(request, 'payments.html', {'payments_T': True})


def view_guide(request):
    if request.method == 'GET':
        filtered_guides = TourGuide.objects.filter(user__city=request.user.city)
        context = {'guides': filtered_guides}
        return render(request, 'render_guides.html', context)
    else:
        return redirect('home')


def trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            gender = form.cleaned_data['gender']
            state = form.cleaned_data['state']
            city = form.cleaned_data['city']
            days = form.cleaned_data['days']
            languages = form.cleaned_data['languages']
            qualities = form.cleaned_data['qualities']
            user = User.objects.get(username=request.user.username)
            user.gender = gender
            user.city = city
            user.state = state
            user.gender = gender
            user.personality_traits = languages
            user.languages = qualities
            user.save()
            return view_guide(request)
    else:
        form = TripForm()
    return render(request, 'trip.html', {'form': form, 'no_footer': True})

def guide(request):
    if request.method == 'POST':
        form = GuideForm(request.POST)
        if form.is_valid():
            gender = form.cleaned_data['gender']
            state = form.cleaned_data['state']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone_number']
            make = form.cleaned_data['make']
            model = form.cleaned_data['model']
            license_plate = form.cleaned_data['license_plate']
            languages = form.cleaned_data['languages']
            qualities = form.cleaned_data['qualities']
            # Do something with the data
            return redirect('home')
    else:
        form = TripForm()
    return render(request, 'guide.html', {'form': form, 'no_footer': True, 'guide_T': True})

        