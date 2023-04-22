from django.shortcuts import render, redirect, reverse
from django.views.generic import View
import environ

env = environ.Env()
environ.Env.read_env()


def landing_page(request):
    return render(request, 'homepage.html')