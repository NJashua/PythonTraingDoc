# movies/models.py
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    description = models.TextField()
    poster = models.ImageField(upload_to='posters/')

    def __str__(self):
        return self.title

class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    show_time = models.DateTimeField()
    theater = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.movie.title} - {self.theater} - {self.show_time}"