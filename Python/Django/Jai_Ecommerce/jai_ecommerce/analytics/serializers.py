from rest_framework import serializers

class SalesDataSerializer(serializers.Serializer):
    order_date = serializers.DateField()
    total_sales = serializers.DecimalField(max_digits=10, decimal_places=2)
