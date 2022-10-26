from django.db import models

# Create your models here.
class Artist(models.Model):
    first_naeme = models.CharField(max_length=100)
    last_naeme = models.CharField(max_length=100)
    age = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.first_naeme} {self.last_naeme}"
    
class Song(models.Model):
    title = models.CharField(max_length=100, blank=False)
    date_released = models.DateTimeField() 
    likes = models.IntegerField()
    artiste_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title
    
class Lyrics(models.Model):
    content = models.TextField()
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.content