# from rest_framework import viewsets
# from .models import Product, Customer, Order
# from .serializers import ProductSerializer, CustomerSerializer, OrderSerializer

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class CustomerViewSet(viewsets.ModelViewSet):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer

# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer


# store/views.py

# from rest_framework import viewsets, status
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from .models import Product, Customer, Order
# from .serializers import ProductSerializer, CustomerSerializer, OrderSerializer

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class CustomerViewSet(viewsets.ModelViewSet):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer

# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

#     @action(detail=False, methods=['post'])
#     def order_product(self, request):
#         customer_id = request.data.get('customer')
#         product_id = request.data.get('product')
#         quantity = int(request.data.get('quantity'))

#         try:
#             customer = Customer.objects.get(id=customer_id)
#             product = Product.objects.get(id=product_id)

#             if product.stock < quantity:
#                 return Response({'status': 'error', 'message': 'Insufficient stock'}, status=status.HTTP_400_BAD_REQUEST)

#             total_price = product.price * quantity
#             order = Order(customer=customer, product=product, quantity=quantity, total_price=total_price)
#             order.save()

#             # Update product stock
#             product.stock -= quantity
#             product.save()

#             return Response({'status': 'success', 'order_id': order.id}, status=status.HTTP_201_CREATED)
#         except Customer.DoesNotExist:
#             return Response({'status': 'error', 'message': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)
#         except Product.DoesNotExist:
#             return Response({'status': 'error', 'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

# store/views.py

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Product, Customer, Order
from .serializers import ProductSerializer, CustomerSerializer, OrderSerializer, OrderCreateSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

@api_view(['POST'])
def order_product(request):
    serializer = OrderCreateSerializer(data=request.data)
    if serializer.is_valid():
        order = serializer.save()
        return Response({'status': 'success', 'order_id': order.id}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

