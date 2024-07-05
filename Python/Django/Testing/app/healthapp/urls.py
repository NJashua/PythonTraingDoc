from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData, name='get-data'),
    path('post/', views.postData, name='post-data'),
    path('hello/', view=views.HelloWorld.as_view(), name='hello_world'),
]
