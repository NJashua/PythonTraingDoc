#2. Write a program that accepts a list from user. Your program should reverse the content of list and display it. Do not use reverse() method.

list_a = input("Enter a valid list items: ").split(",")

reverse_list = list_a[::-1]
print("List before shifting..:", list_a)
print("The reverse list is", reverse_list)