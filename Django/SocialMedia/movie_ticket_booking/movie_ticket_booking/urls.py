# movie_ticket_booking/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
    path('booking/', include('booking.urls')),
    path('users/', include('users.urls')),
]