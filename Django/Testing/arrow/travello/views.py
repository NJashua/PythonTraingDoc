from django.shortcuts import render
from travello.models import Destination

def travello(request):
    dest1 = Destination()
    dest1.name = "Agra"
    dest1.desc = "The best place to visit"
    return render(request, 'index.html', {'dest1': dest1})
