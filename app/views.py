from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
import environ
# TODO 
env = environ.Env()
environ.Env.read_env()


def landing_page(request):
    return render(request, 'homepage.html')

def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

            
    context = {'form': form}
    return render(request, 'signup.html', context)