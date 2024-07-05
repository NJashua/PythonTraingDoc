# booking/models.py
from django.db import models
from movies.models import Show

class Booking(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.show} - {self.seat_number} - {self.user}"