from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def home(request):
    james = loader.get_template('myfirst.html')
    return HttpResponse(james.render())