# api/models.py

from django.db import models

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='audio/')

    def __str__(self):
        return self.title
