# mysite/hey/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.microsoft_login_page, name='microsoft_login_page'),  # Route root URL to microsoft_login_page view
]
