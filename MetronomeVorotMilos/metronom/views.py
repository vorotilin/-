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


from .models import MetronomeSettings

@login_required
def metronome_settings_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        range = request.POST.get('speed-range')
        counter_bottom = request.POST.get('counter-bottom')
        counter_top = request.POST.get('counter-top')

        
        setting = MetronomeSettings( user=request.user, name=name, range=range, counter_bottom=counter_bottom, counter_top=counter_top)
        setting.save()
        return redirect('metronome_settings')

    # Обработка GET-запроса для отображения формы
    settings = MetronomeSettings.objects.all()  # Получаем все настройки для отображения
    return render(request, 'metronom/home.html', {'settings': settings})

def use_metronome(request, setting_id):
    setting = MetronomeSettings.objects.get(id=setting_id, user=request.user)
    # Здесь вы можете передать настройки в шаблон или использовать их в логике приложения
    return render(request, 'home.html', {'setting': setting})

# Create your views here.


