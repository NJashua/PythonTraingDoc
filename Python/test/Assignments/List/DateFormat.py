#6. Write a program that reads a string from the user containing a date in the form mm/dd/yyyy. It should print the date in the form March 12, 2021.

date_str = input("Enter a date in the format mm/dd/yyyy: ")

date= date_str.split('/')

months_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

month = int(date[0])
day = int(date[1])
year = int(date[2])

formatted_month = months_names[month - 1]


formatted_date = f"{formatted_month} {day}, {year}"
print("Formatted date:", formatted_date)
