# File: roombooking_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin interface
    path('', include('rooms.urls')),  # Include URLs from the 'rooms' app
]
