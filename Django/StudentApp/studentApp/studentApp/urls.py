# studentApp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.input_form, name='input-form'),
]
