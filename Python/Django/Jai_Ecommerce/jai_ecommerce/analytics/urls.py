# analytics/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('sales-report/', views.sales_report, name='sales_report'),
    path('api/sales-report/', views.sales_report_api, name='sales_report_api'),
]
