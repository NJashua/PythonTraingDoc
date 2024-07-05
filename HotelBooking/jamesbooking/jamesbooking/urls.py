# urls.py

from django.contrib import admin
from django.urls import path, include
from bookings import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('bookings.urls')),
]
