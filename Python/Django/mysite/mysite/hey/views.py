# mysite/hey/views.py
from django.shortcuts import render

def microsoft_login_page(request):
    return render(request, 'index.html')
