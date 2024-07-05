$(document).ready(function() {
    loadBookingHistory();
    loadRoomStats();

    function loadBookingHistory() {
        $.ajax({
            url: '/api/bookings/',
            method: 'GET',
            success: function(data) {
                let bookingHistory = $('#booking-history');
                bookingHistory.empty();
                data.forEach(function(booking) {
                    bookingHistory.append(`<li>${booking.hotel.name} - ${booking.checkin_date} to ${booking.checkout_date}</li>`);
                });
            }
        });
    }

    function loadRoomStats() {
        $.ajax({
            url: '/api/hotels/',
            method: 'GET',
            success: function(data) {
                let roomStats = $('#room-stats');
                roomStats.empty();
                data.forEach(function(hotel) {
                    roomStats.append(`<div>${hotel.name} - ${hotel.rating} stars - $${hotel.price} per night</div>`);
                });
            }
        });
    }
});
