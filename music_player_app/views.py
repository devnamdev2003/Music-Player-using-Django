# music_player_app/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm, LoginForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'music_player_app/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'music_player_app/login.html', {'form': form})


@login_required
def index(request):
    return render(request, 'music_player_app/index.html')


@login_required
def AddSong(request):
    return render(request, 'music_player_app/AddSong.html')


@login_required
def UpdateSong(request, pk):
    return render(request, 'music_player_app/UpdateSong.html')
