import pandas as pd
from store.models import Product, Order, Customer
from .mysql_utils import get_snowflake_connection

def ingest_data_to_snowflake():
    conn = get_snowflake_connection()
    cursor = conn.cursor()

    # Ingest products data
    products = Product.objects.all().values()
    df_products = pd.DataFrame(list(products))
    cursor.write_pandas(df_products, 'PRODUCTS')

    # Ingest customers data
    customers = Customer.objects.all().values()
    df_customers = pd.DataFrame(list(customers))
    cursor.write_pandas(df_customers, 'CUSTOMERS')

    # Ingest orders data
    orders = Order.objects.all().values()
    df_orders = pd.DataFrame(list(orders))
    cursor.write_pandas(df_orders, 'ORDERS')

    cursor.close()
    conn.close()
