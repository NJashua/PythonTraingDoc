# store/serializers.py

from rest_framework import serializers
from .models import Product, Customer, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderCreateSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()

    def validate(self, data):
        try:
            customer = Customer.objects.get(pk=data['customer_id'])
        except Customer.DoesNotExist:
            raise serializers.ValidationError("Customer not found")
        
        try:
            product = Product.objects.get(pk=data['product_id'])
        except Product.DoesNotExist:
            raise serializers.ValidationError("Product not found")

        if product.stock < data['quantity']:
            raise serializers.ValidationError("Not enough stock available")

        return data

    def create(self, validated_data):
        customer = Customer.objects.get(pk=validated_data['customer_id'])
        product = Product.objects.get(pk=validated_data['product_id'])
        order = Order.objects.create(
            customer=customer,
            product=product,
            quantity=validated_data['quantity'],
            total_price=product.price * validated_data['quantity']
        )
        product.stock -= validated_data['quantity']
        product.save()
        return order
