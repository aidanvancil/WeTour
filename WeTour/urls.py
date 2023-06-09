"""
URL configuration for WeTour project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='landing_page'),
    path('home', views.homepage, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.login, name='logout'),
    path('profile', views.profile, name='profile'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('about', views.about_us, name='about'),
    path('trip', views.trip, name='trip'),
    path('trip/<int:param>', views.trip, name='tript'),
    path('render_guides', views.view_guide, name='render_guides'),
    path('guide', views.guide, name='guide'),
    path('card', views.card, name='card'),
    path("__reload__/", include("django_browser_reload.urls")),
]
