from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, HotelViewSet, BookingViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'hotels', HotelViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
