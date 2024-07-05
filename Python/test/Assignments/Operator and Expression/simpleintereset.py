# 4. Write a program which accept principle, rate and time from user and print the simple interest. 
# The formula to calculate simple interest is: simple interest = principle x rate x time / 100 

principle_amount = int(input("Enter valid principle amount: "))
rate_amount = float(input("Enter valid rate amount: "))
time_details = int(input("Enter no.of months: "))

month_conversion = time_details/12

cal_simple_interest = (principle_amount * rate_amount * month_conversion)/100
print(f"Simple interest is ", cal_simple_interest)