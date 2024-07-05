import sqlite3 as covid

connection = covid.connect("Assignments/DatabaseOperations/data.db")
cursor = connection.cursor()

def create_table():
    table_data = []
    table_name = input("Enter table name: ")
    while True:
        col_name = input("Enter col name/Enough: ")
        if col_name == "Enough":
            break
        col_type = input("Enter col type: ")
        table_data.append((col_name, col_type))
    sql_statement = f"CREATE TABLE IF NOT EXISTS {table_name} ("
    for column in table_data:
        sql_statement += f"{column[0]} {column[1]}, "
    sql_statement = sql_statement.rstrip(", ") + ")" 

    try:
        cursor.execute(sql_statement)
        connection.commit()
        print("Table has been created")
    except Exception as e:
        print("have a look on", e)
def insert_data():
    table_name = input("Enter table name: ")
    try:
        cursor.execute(f"INSERT INTO {table_name}(ID, NAME, DESTINATION) VALUES (1, 'Nithin', 'MOON')")
        print("data inserted")
        connection.commit()
    except Exception as e:
        print("facing error ", e)
    finally:
        cursor.close()
        connection.close()
def delete_row():
    
def display_tables():
    table_name = input("Enter table name: ")

    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        result_data = cursor.fetchall()
        print(result_data)
    except Exception as eew:
        print("Have a look on",eew)

# create_table()
# insert_data()
display_tables()
delete_row()
connection.close()