# booking/views.py
from rest_framework import viewsets
from .models import Hotel, Room, Booking
from .serializers import HotelSerializer, RoomSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(guest=user)

    def get_queryset(self):
        user = self.request.user
        return Booking.objects.filter(guest=user)
