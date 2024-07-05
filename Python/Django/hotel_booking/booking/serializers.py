# booking/serializers.py
from rest_framework import serializers
from .models import Hotel, Room, Booking
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer()

    class Meta:
        model = Room
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    room = RoomSerializer()
    guest = UserSerializer()

    class Meta:
        model = Booking
        fields = '__all__'
