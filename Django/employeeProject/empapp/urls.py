# empapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_employee, name='display_employee'),
]
