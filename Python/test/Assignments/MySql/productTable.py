# import mysql.connector

# connection = mysql.connector.connect(
#     host = "localhost",
#     username = "root",
#     password = "Jashua@9390779404",
#     database = "training"
# )
# product_data = [
#     (1, "Dell Mouse", 1200),
#     (2, "Lenovo Laptop", 25000),
#     (3, "HP Keyboard", 1500),
#     (4, "Apple MacBook Pro", 98000),
#     (5, "Samsung Monitor", 18000),
#     (6, "Sony Headphones", 4500),
#     (7, "Logitech Webcam", 3500),
#     (8, "Acer Aspire Desktop", 32000),
#     (9, "Microsoft Surface Pro", 55000),
#     (10, "Asus ROG Gaming Laptop", 75000),
#     (11, "LG UltraWide Monitor", 28000),
#     (12, "Razer Gaming Mouse", 6000),
#     (13, "Intel Core i9 Processor", 35000),
#     (14, "Corsair Mechanical Keyboard", 8000),
#     (15, "Google Pixelbook", 70000),
#     (16, "Bose Noise Cancelling Headphones", 25000),
#     (17, "Canon DSLR Camera", 45000),
#     (18, "Western Digital External HDD", 6000),
#     (19, "Nvidia GeForce RTX 3080 GPU", 85000),
#     (20, "Apple iPad Pro", 60000),
#     (21, "Brother Laser Printer", 12000),
#     (22, "Huawei MateBook X Pro", 58000),
#     (23, "JBL Bluetooth Speaker", 4000),
#     (24, "Seagate Barracuda SSD", 10000),
#     (25, "Xiaomi Mi Curved Gaming Monitor", 30000),
#     (26, "AMD Ryzen 9 Processor", 32000),
#     (27, "Dell XPS 15 Laptop", 80000),
#     (28, "Samsung Galaxy Tab S7", 55000),
#     (29, "Philips Hue Smart Bulbs Starter Kit", 6000),
#     (30, "Logitech G Pro Wireless Gaming Mouse", 12000),
#     (31, "Asus ZenBook Flip", 6500)]

# hey_cursor = connection.cursor()

# def create_table_insert_data():
#     try:
#         if connection:
            
#             hey_cursor.execute("USE TRAINING")
#             print("Using training database")
#             # hey_cursor.execute("CREATE TABLE PRODUCT(pid INT, pname VARCHAR(200), price FLOAT)")
#             # print("table created..!!!")
#             #insert data into product table...:)
#             insert_query = f"INSERT INTO PRODUCT(pid, pname, price) VALUES (%s, %s, %s)"
#             # hey_cursor.execute(insert_query%product_data)
#             hey_cursor.executemany(insert_query, product_data)
#             connection.commit()
#             print("Data inserted into product table and have a look on workbench or mysql terminal..!!!")
#     except ConnectionError as e:
#         print("Connection check chesko..bro",e)
#     except Exception as james:
#         print("Getting error", james)
#     finally:
#         connection.close()
#         hey_cursor.close()

# def insert_a_single_row():
#     try:
#         if connection:
#             print("Connected")
#             hey_cursor.execute("INSERT INTO PRODUCT(PID, PNAME, PRICE) VALUES(4, 'Clock Har', 500)")
#             print("A single row inserted into product table..have a look on workbench")
#     except ConnectionError as check:
#         print("Check the connection man...", check)
#     except Exception as checked:
#         print("Getting unknown error..", checked)
#         connection.commit()
#     finally:
#         connection.close()
#         hey_cursor.close()

# def get_rows_in_table():
#     try:
#         if connection:
#             hey_cursor.execute("SELECT * FROM PRODUCT")
#             #value = hey_cursor.fetchall()
#             value = hey_cursor.fetchmany(1)
#             print("Selected data is..:")
#             for data in value:
#                 print("product id is: ", data[0])
#                 print("product Name is : ",data[1])
#                 print("product Price is : ",data[2])
#             # print(value)
#     except Exception as e:
#         print("Have a look on error", e)

# def insert_multiple_rows():
#     try:
#         if connection:
#             print("Connection succeed")
#             insert_query = f"INSERT INTO PRODUCT(pid, pname, price) VALUES (%s, %s, %s)"
#             hey_cursor.executemany(insert_query, product_data)
#             print("Multiple data inserted into product table...:)")
#             connection.commit()

#     except Exception as e:
#         print("Have a look on error", e)
#     finally:
#         connection.close()
#         hey_cursor.close()

# def delete_row_in_table():
#     try:
#         if connection:
#             print("Connection S")
# #create_table_insert_data()
# #insert_a_single_row()
# # get_rows_in_table()
# # insert_multiple_rows()
# delete_row_in_table()