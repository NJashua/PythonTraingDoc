# booking/admin.py

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Location, Room, Booking

# Unregister the default UserAdmin
admin.site.unregister(User)

# Define your CustomUserAdmin
class CustomUserAdmin(UserAdmin):
    pass  # Add your customizations here

# Register User with your CustomUserAdmin
admin.site.register(User, CustomUserAdmin)

# Register your other models
admin.site.register(Location)
admin.site.register(Room)
admin.site.register(Booking)
