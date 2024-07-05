from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', views.EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='employee-retrieve-update-destroy'),
]
