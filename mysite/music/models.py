from django.db import models 

class Album(models.Model):
    artist = models.CharFiel(max_lenght=500)
    albun_title = models.CharFiel(max_lenght=500)
    genre = models.CharField(max_length = 100)
    album_logo = models.CharField(max_length=1000)

class Song(models.Models):
    album = models.ForeighKey(Album, on_delete=models.CASCADE) #when an album is deleted all the songs attached to this ablbum will be deleted aswell
    file_type = models.CharField(max_lenght=10)
    song_title = models.CharField(max_lenght=250)
