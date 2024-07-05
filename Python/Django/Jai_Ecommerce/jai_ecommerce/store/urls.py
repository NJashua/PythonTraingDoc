# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import ProductViewSet, CustomerViewSet, OrderViewSet

# router = DefaultRouter()
# router.register(r'products', ProductViewSet)
# router.register(r'customers', CustomerViewSet)
# router.register(r'orders', OrderViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

# store/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CustomerViewSet, OrderViewSet, order_product

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('orders/order_product/', order_product, name='order_product'),
]