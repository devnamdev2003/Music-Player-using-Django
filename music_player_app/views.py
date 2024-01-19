# music_player_app/views.py

from django.shortcuts import render, redirect
from .models import Song


def song_list(request):
    songs = Song.objects.all()
    return render(request, 'music_player_app/index.html', {'songs': songs})
