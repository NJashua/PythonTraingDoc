from django.contrib import admin
from .models import User, Hotel, Booking, Transaction

admin.site.register(User)
admin.site.register(Hotel)
admin.site.register(Booking)
admin.site.register(Transaction)
