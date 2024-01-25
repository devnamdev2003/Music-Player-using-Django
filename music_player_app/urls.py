# music_player_app/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from music_player_app.views import register, user_login
from music_player_app.views import index, UpdateSong, AddSong

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
    path('home', index, name='home'),
    path('UpdateSong/<int:pk>', UpdateSong, name='UpdateSong'),
    path('AddSong', AddSong, name='AddSong'),
]
