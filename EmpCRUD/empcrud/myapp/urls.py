# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.department_list, name='department_list'),
    path('department/<int:pk>/', views.department_detail, name='department_detail'),
    path('department/create/', views.department_create, name='department_create'),
    path('department/<int:pk>/update/', views.department_update, name='department_update'),
    path('department/<int:pk>/delete/', views.department_delete, name='department_delete'),
    path('department/<int:pk>/employee/create/', views.employee_create, name='employee_create'),
    path('employee/<int:pk>/update/', views.employee_update, name='employee_update'),
    path('employee/<int:pk>/delete/', views.employee_delete, name='employee_delete'),
    path('employee/search/', views.employee_search, name='employee_search'),
]
