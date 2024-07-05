from django.urls import path
from . import views

urlpatterns = [
    path('todos/api/', views.TodoListApiView.as_view(), name='todo_list_api'),
    path('todos/api/<int:pk>/', views.TodoDetailApiView.as_view(), name='todo_detail_api'),
]
