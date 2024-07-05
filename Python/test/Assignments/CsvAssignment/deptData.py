import csv 

with open("deptData.csv", 'w', newline="") as file:
    writer = csv.writer(file)
    writer.writerow(['EID', 'ENAME', 'ELOCATION'])
    dept_id = int(input("Enter id val: "))
    dept_name = input("Enter dept name: ")
    location_name = input("Enter location name: ")
    writer.writerow([dept_id, dept_name, location_name])
    print("data inserted...!!!")