import csv 
import sqlite3

# with open("deptData.csv", "r") as file:
#     james = csv.reader(file)
    
connection = sqlite3.connect("C:\\data\\ecOnSqlite.sqlite3")
my_cursor = connection.cursor()

# my_cursor.execute("CREATE TABLE DEPT(DEPTNO INT, DEPTNAME VARCHAR(250), DEPTLOC VARCHAR(250))")
# print("table is created")
# for row in james:
#     my_cursor.execute("INSERT INTO DEPT (DEPTNO, DEPTNAME, DEPTLOC) VALUES (?, ?, ?)", row)

my_cursor.execute("SELECT * FROM DEPT")
value = my_cursor.fetchall()
list_a = []
for row in value:
    list_a.append(row)
with open("Hey.csv", mode='r', newline="") as file:
    # james = csv.writer(file)
    # james.writerow(list_a)
    # print("data inserted into new file")
    value = file.read()
    print(value)
    
connection.commit()