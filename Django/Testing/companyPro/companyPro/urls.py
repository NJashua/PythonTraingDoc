from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('companies/', views.CompanyListView.as_view(), name='companies'),
    path('<int:pk>/', views.CompanyDetailView.as_view(), name='detail'),
    path('create/', views.CompanyCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.CompanyUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.CompanyDeleteView.as_view(), name='delete'),
]
