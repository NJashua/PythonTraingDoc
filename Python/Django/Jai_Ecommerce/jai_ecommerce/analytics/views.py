# analytics/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .mysql_utils import get_mysql_connection
import pandas as pd
import plotly.express as px

def sales_report(request):
    conn = get_mysql_connection()
    query = "SELECT order_date, SUM(total_price) as total_sales FROM store_order GROUP BY order_date ORDER BY order_date"
    sales_data = pd.read_sql(query, conn)
    fig = px.line(sales_data, x='order_date', y='total_sales', title='Sales Over Time')
    graph = fig.to_html(full_html=False)
    context = {'graph': graph}
    return render(request, 'analytics/sales_report.html', context)

def sales_report_api(request):
    try:
        conn = get_mysql_connection()
        query = "SELECT order_date, SUM(total_price) as total_sales FROM store_order GROUP BY order_date ORDER BY order_date"
        sales_data = pd.read_sql(query, conn)
        data = sales_data.to_dict(orient='records')
        return JsonResponse({'status': 'success', 'data': data}, status=200)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
