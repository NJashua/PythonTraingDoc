# 6. Write a program that prompts the user to enter number in two variables and swap the contents of the variables. 

a = input("Enter a number or word: ")
b = input("Enter a number or word: ")

print(f"Before swapping elements: {a}, {b}")

new_val_copy = a
a = b
b = new_val_copy

print(f"After swapping elements: {a}, {new_val_copy}")