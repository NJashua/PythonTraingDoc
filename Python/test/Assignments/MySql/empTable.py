import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Jashua@9390779404'
)

hey_cursor = connection.cursor()
def create_database():
    try:
        db_name = input("Enter database name: ")
        hey_cursor.execute(f"CREATE DATABASE {db_name}")
        print("Database has been created")
    except:
        print("check code facing error..!!!")
def create_table():
    try:
        db_name = input("Enter database name: ")
        table_name = input("Enter table name: ")
        hey_cursor.execute(f"USE {db_name}")
        hey_cursor.execute(f"CREATE TABLE {table_name} (eid INT AUTO_INCREMENT PRIMARY KEY, ename VARCHAR(255), sal VARCHAR(255))")
        print("table created successfully...!!!")
    except Exception as e:
        print("Facing error", e)
    

# create_database()
create_table()