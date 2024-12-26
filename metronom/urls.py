from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from .views import home, register, logout_view

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('submit/', lambda request: (
        User.objects.create(
            range=request.POST.get('range'),
            counter_bottom=request.POST.get('counter_bottom'),
            counter_top=request.POST.get('counter_top')
        ) if request.method == 'POST' else HttpResponse('Метод не разрешен', status=405),
        HttpResponse('Данные успешно сохранены')
    )[1]),
]