from django import forms
from .models import Customer, Product, Order

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'  # Or specify fields explicitly

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'  # Or specify fields explicitly

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'  # Or specify fields explicitly
