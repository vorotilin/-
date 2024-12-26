from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html', {'user': request.user})
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserLoginForm()
    
    return render(request, 'home.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'register.html', {'form': form})


@login_required
def profile_view(request):
    user = request.user  # Получаем текущего аутентифицированного пользователя
    return render(request, 'profile.html', {'user': user})


@login_required
def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('home')

# Create your views here.
