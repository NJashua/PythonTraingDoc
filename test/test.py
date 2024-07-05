import sqlite3

try:

    # data
    products = [
        (1, 'Widget', 19.99, 'Gadgets'),
        (2, 'Gizmo', 29.99, 'Gadgets'),
        (3, 'Doodad', 9.99, 'Accessories')
    ]

# Inserting multiple rows using %s placeholders
    conn = sqlite3.connect("C:\\data\\ecOnSqlite.sqlite3")
    my_cur = conn.cursor()
    #my_cur.execute("CREATE TABLE PRODUCT(P_ID INT, PNAME VARCHAR(250), PRICE FLOAT)")
    # for product in products:
    #     # my_cur.execute("""INSERT INTO PRODUCT(P_ID, PNAME, PRICE, CATEGORY) VALUES (%d, %s, %d, %s)""", product)
    #     my_cur.execute("""INSERT INTO PRODUCT(P_ID, PNAME, PRICE, CATEGORY) VALUES (%s, %s, %s, %s)""", product)
    #     print("data inserted successfully")
    my_cur.execute("SELECT * FROM PRODUCT")
    # my_cur.execute("UPDATE PRODUCT SET PNAME = 'KAKARA KAAYA', PRICE = 50 WHERE PNAME = 'apple'")
    #my_cur.execute("DELETE FROM PRODUCT WHERE PNAME = 'papaya'")
    # my_cur.execute("ALTER TABLE PRODUCT ADD COLUMN CATEGORY VARCHAR(250)")
    # my_cur.execute("INSERT INTO PRODUCT (CATEGORY) VALUES ('fruit')")
    value= my_cur.fetchall()
    # for i in value:   
    # print(value)
    # sql = """INSERT INTO PRODUCT(P_ID, PNAME, PRICE, CATEGORY) VALUES (%d, %s, %f, %s)"""
    # my_cur.executemany(sql, products)

    # p_id = int(input("Enter id value: "))
    # p_name = input("Enter product name: ")
    # p_price = int(input("Enter price: "))
    # p_category = input("Enter category: ")

    # command = "INSERT INTO PRODUCT VALUES(%d, '%s', %d, '%s')" % (p_id, p_name, p_price, p_category)
    # my_cur.execute(command)
    # print("Data inserted into product successfully")
    print(value)
    # print("data updated with the new name kakara kaaya")
    conn.commit()
except sqlite3.DatabaseError as james:
    print(f"Facing connection error: {james}")
finally:
    if my_cur:
        my_cur.close()
    if conn:
        conn.close()
