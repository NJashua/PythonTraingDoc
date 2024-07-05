# EmployeeManagement/urls.py
from django.contrib import admin
from django.urls import path, include
from EmpView import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('employees/', views.EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
        path('employees/<int:pk>/', views.EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='employee-retrieve-update-destroy'),
    ])),
]
