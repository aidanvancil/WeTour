from django.shortcuts import render, redirect, reverse
from app.forms import UserFormCreation, TripForm, GuideForm, ProfileRegisterForm
from app.models import TourGuide, Profile, Trip
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages





def landing_page(request):
    context = {'background_color': '#000000'}
    return render(request, 'landing_page.html', context)


def spawn_trips():
    users = User.objects.all()
    profiles = []
    for user in users:
        profiles.append(Profile.objects.filter(user=user))
    return user, profiles

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
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect('home')
        else:
            error_message = "Username or password is incorrect."
            print(error_message)
            context = {'error_message': error_message}
            return render(request, 'login.html', context)
    print("bruh")
    return render(request, 'login.html')

@login_required(login_url='login')
def logout(request):
    logout(request)
    return redirect('login')

def homepage(request):
    users, profiles = spawn_trips()

    # results = []
    # for profile in profiles:
    #     for trait in profile.personality_traits:
    #         if trait in 

    return render(request, 'homepage.html', {'homepage_T': True, 'users': users, 'profiles': profiles})

def profile(request):
    
    profile = Profile.objects.filter(user=request.user)
    user = User.objects.filter(username=request.user)
    print(profile[0].user)
    print(user[0].username)
    

    return render(request, 'profile.html', {'no_footer': True, 'profile_T': True, 'profile': profile[0], 'user': user[0]})

def about_us(request):
    return render(request, 'aboutus.html', {'no_footer': True, 'profile_T': True})

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
            biography = form.cleaned_data['biography']
            user = User.objects.filter(username=request.user)
            user.gender = gender
            user.city = city
            user.state = state
            user.gender = gender
            user.personality_traits = languages
            user.languages = qualities
            user.biography = biography
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
            biography = form.cleaned_data['biography']
            response = co.summarize(text=bio)
            print(response)
            # Do something with the data
            


            return redirect('home')
    else:
        form = TripForm()
    return render(request, 'guide.html', {'form': form, 'no_footer': True, 'guide_T': True})

def sub_trip(request):
    user = request.user 
    return render(request, 'sub_trip.html', {'form': form, 'no_footer': True})

        