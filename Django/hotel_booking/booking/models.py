# booking/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    amenities = models.TextField()
    image = models.ImageField(upload_to='hotels/', default='hotels/default_hotel.jpg')

    def __str__(self):
        return self.name

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    room_number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"Room {self.room_number} at {self.hotel.name}"

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    num_of_persons = models.IntegerField()

    def __str__(self):
        return f"{self.guest.username} - {self.room}"
