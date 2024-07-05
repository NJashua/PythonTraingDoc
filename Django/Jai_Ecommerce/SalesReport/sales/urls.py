from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.CustomerViewSet.as_view({'get': 'list', 'post': 'create'}), name='customer-list'),
    path('customers/<int:pk>/', views.CustomerViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='customer-detail'),
    
    path('products/', views.ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='product-list'),
    path('products/<int:pk>/', views.ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='product-detail'),
    
    path('orders/', views.OrderViewSet.as_view({'get': 'list', 'post': 'create'}), name='order-list'),
    path('orders/<int:pk>/', views.OrderViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='order-detail'),

    path('monthly-sales/', views.monthly_sales, name='monthly-sales'),

    path('add-customer/', views.add_customer, name='add-customer'),
    path('add-product/', views.add_product, name='add-product'),
    path('add-order/', views.add_order, name='add-order'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete-product')

]
