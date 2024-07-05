from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    movie_name = models.CharField(max_length=100)
    movie_description = models.TextField()
    movie_image = models.CharField(max_length=500)
    price = models.IntegerField()
    release_date = models.DateField()
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.movie_name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    show = models.ForeignKey('Show', on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)
    booking_time = models.TimeField(auto_now_add=True)
    seat_number = models.CharField(max_length=10)
    payment_status = models.BooleanField(default=False)

class Theater(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    show_date = models.DateField()
    show_time = models.TimeField()
    available_seats = models.IntegerField()

    def __str__(self):
        return f"{self.movie.movie_name} - {self.theater.name} - {self.show_date} - {self.show_time}"