# 3. Write a program that prompts the user to input a Celsius temperature and outputs the equivalent temperature in Fahrenheit. The formula to convert the temperature is: F = 9/5 C + 32 where F is the Fahrenheit temperature and C is the Celsius temperature. 

temp = int(input("Enter temp: "))

f = 9/5 * temp + 32
print("Fahrenheit temperature is", f)