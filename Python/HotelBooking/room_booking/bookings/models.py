from django.db import models
from django.contrib.auth.models import AbstractUser
import random

def random_price():
    return random.randint(800, 2000)

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='bookings_user_set',  # Changed related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='bookings_user_set',  # Changed related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username
class Hotel(models.Model):
    city = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    overview = models.CharField(max_length=64)
    highlight = models.CharField(max_length=64)
    room_types = models.CharField(max_length=64)
    rating = models.CharField(max_length=64)
    price = models.FloatField(default=random_price)
    imgurls = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} - {self.name}"

class Booking(models.Model):
    hotel = models.ForeignKey(Hotel, related_name="bookings", on_delete=models.CASCADE)
    tracking_id = models.CharField(max_length=64, default='000')
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    phone = models.CharField(max_length=15)
    room = models.IntegerField(default=1)
    adult = models.IntegerField(default=1)
    child = models.IntegerField(default=0)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    booking_date = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(default=None)
    user = models.ForeignKey(User, related_name="bookings", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.tracking_id

class Transaction(models.Model):
    made_by = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        super().save(*args, **kwargs)
