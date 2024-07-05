# healthapp/views.py

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Data
from .serializer import DataSerializer
from django.views.generic import View, TemplateView
from django.http import HttpResponse
# from healthapp.models import 

@api_view(['GET'])
def getData(request):
    app = Data.objects.all()
    serializer = DataSerializer(app, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postData(request):
    serializer = DataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
class HelloWorld(View):
    def get(self, request):
        return HttpResponse("<h1>Hello James Bond</h1>")
    

# class Veiew_Data(View):
