from django.urls import path
from . import views

urlpatterns = [
    path('rooms/', views.RoomListView.as_view(), name='room-list'),
    path('rooms/<int:id>/', views.RoomDetailView.as_view(), name='room-detail'),
    path('book/', views.BookRoomView.as_view(), name='book-room'),
    path('booking/history/', views.booking_history, name='booking-history'),
]
