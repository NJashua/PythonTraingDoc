from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import redirect, render
from .models import Customer, Product, Order
from .forms import CustomerForm, ProductForm, OrderForm
from django.utils.timezone import now
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from rest_framework import viewsets
from .serializers import CustomerSerializer, ProductSerializer, OrderSerializer
from django.utils import timezone

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

@api_view(['GET'])
def monthly_sales(request):
    one_month_ago = timezone.now() - pd.DateOffset(months=1)
    
    orders = Order.objects.filter(order_date__gte=one_month_ago)

    data = []
    for order in orders:
        data.append({
            'order_date': order.order_date.strftime('%Y-%m-%d'), 
            'quantity': order.quantity,
            'product': order.product.name,
            'category': order.product.category
        })

    df = pd.DataFrame(data)

    sales_summary = df.groupby(df['order_date'])['quantity'].sum()

    # Data visualization
    fig, ax = plt.subplots()
    sales_summary.plot(kind='bar', ax=ax)
    ax.set_title('Monthly Sales Summary')
    ax.set_xlabel('Date')
    ax.set_ylabel('Quantity Sold')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    image_png = buf.getvalue()
    buf.close()

    image_base64 = base64.b64encode(image_png).decode('utf-8')

    return Response({'sales_summary': sales_summary.to_dict(), 'image': image_base64})

@api_view(['POST'])
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer-list')  
    else:
        form = CustomerForm()

    return render(request, 'crud.html', {'form': form})

@api_view(['POST'])
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product-list')  # Redirect to product list URL
    else:
        form = ProductForm()

    return render(request, 'crud.html', {'form': form})

@api_view(['POST'])
def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order-list')  # Redirect to order list URL
    else:
        form = OrderForm()

    return render(request, 'crud.html', {'form': form})

@api_view(['DELETE'])
def delete_product(request):
    if request.method == 'DELETE':
        try:
            product_id = request.data.get('id')
            product = Product.objects.get(id = id)
            product.delete()
            return Response({"msg": "Product deleted"})
        except Exception as msg:
            print("getting error while deleting", msg)


# @api_view(['DELETE'])
# def delete_product(request):
#     if request.method == 'DELETE':
#         try:
#             product_id = request.data.get('id') 
#             product = Product.objects.get(id=product_id)
#             product.delete()
#             return JsonResponse({'message': 'Product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
#         except Product.DoesNotExist:
#             return JsonResponse({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#     else:
#         return JsonResponse({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
