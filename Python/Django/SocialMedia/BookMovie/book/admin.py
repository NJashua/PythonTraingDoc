from django.contrib import admin
from .models import Movie, Theater, Show

admin.site.register(Movie)
admin.site.register(Theater)
admin.site.register(Show)