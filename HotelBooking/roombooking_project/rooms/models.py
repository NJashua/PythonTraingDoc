# rooms/models.py

from django.db import models

class Room(models.Model):
    ROOM_TYPES = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
    ]

    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES, default='single')
    capacity = models.IntegerField(default=2)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.room_number} - {self.get_room_type_display()}"

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100)
    guest_email = models.EmailField()
    check_in = models.DateField()
    check_out = models.DateField()
    guests_count = models.IntegerField(default=1)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.guest_name} - Room {self.room.room_number}"
