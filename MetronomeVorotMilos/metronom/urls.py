from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from .views import home, register, logout_view
from .views import metronome_settings_view
from .views import use_metronome

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('', metronome_settings_view, name='metronome_settings'),
    path('use/<int:setting_id>', use_metronome, name='use_metronome'),
]



