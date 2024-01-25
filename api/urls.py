# api/urls.py

from django.urls import path
from .views import SongListCreateView, SongDetailView

urlpatterns = [
    path('songs/', SongListCreateView.as_view(), name='song-list-create'),
    path('songs/<int:pk>/', SongDetailView.as_view(), name='song-detail'),
]
