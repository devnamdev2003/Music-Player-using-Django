# music_player_app/admin.py

from django.contrib import admin
from .models import Song

class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', )
    search_fields = ('title', 'artist')

admin.site.register(Song, SongAdmin)
