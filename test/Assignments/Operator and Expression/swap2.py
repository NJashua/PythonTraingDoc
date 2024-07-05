# 7. Write a program that prompts the user to enter number in two variables and swap the contents of the variables.(Do not declare extra variable.)

a = input("Enter a number or word: ")
b = input("Enter a number or word: ")

print(f"Before swapping elements: {a}, {b}")

# changing var with another var value...:)
a,b = b,a
print(f"After swapping elements: {a}, {b}")