# import sqlite3
# conn = sqlite3.connect("C:\data\ecOnSqlite.py")
# print("connection don", conn)
# conn.close()

import csv 
import sqlite3


connection = sqlite3.connect("C:\data\ecOnSqlite.py")
my_cursor = connection.cursor()

# my_cursor.execute("CREATE TABLE DEPT(DEPTNO INT, DEPTNAME VARCHAR(250), DEPTLOC VARCHAR(250))")
# print("table is created")
# for row in james:
#     my_cursor.execute("INSERT INTO DEPT (DEPTNO, DEPTNAME, DEPTLOC) VALUES (?, ?, ?)", row)
my_cursor.execute("SELECT * FROM DEPT")
value = my_cursor.fetchall()
for row in value:
    print(row)
# print(value)
connection.commit()