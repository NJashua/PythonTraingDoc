from django import forms
from.models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('seat_number',)

class PaymentForm(forms.Form):
    payment_method = forms.CharField(max_length=20)