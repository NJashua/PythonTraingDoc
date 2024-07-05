# Prompt the user to enter a valid number list
input_str = input("Enter a valid number list: ")

# Evaluate the input string as a Python expression to create a list
list_a = eval(input_str)

# Find the maximum number in the list
max_num = list_a[0]
for number in list_a:
    if number > max_num:
        max_num = number

print("The maximum number in the list is:", max_num)

# input_str = input("Enter a valid number list: ")


# list_a = eval(input_str)


# max_num = list_a[0]
# for number in list_a:
#     if number > max_num:
#         max_num = number

# print("The maximum number in the list is:", max_num)
