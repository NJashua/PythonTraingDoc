from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from .models import Room, Booking
from .serializers import RoomSerializer, BookingSerializer, UserSerializer

class RoomListView(generics.ListAPIView):
    queryset = Room.objects.filter(is_booked=False)
    serializer_class = RoomSerializer

class RoomDetailView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_field = 'id'

class BookRoomView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        room_id = self.request.data.get('room_id')
        room = get_object_or_404(Room, id=room_id)
        serializer.save(room=room, user=self.request.user)
        room.is_booked = True
        room.save()

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def booking_history(request):
    user = request.user
    bookings = Booking.objects.filter(user=user)
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)
