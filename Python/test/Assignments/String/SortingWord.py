# 4)write a program to sort the characters of the string and print first Alphabet
#  symbol followed by numeric values.
#  input : B4A1D3
#  output : ABD134

input_string = input("Enter a string: ")
alpha_chars = []
number_chars = []
for char in input_string:
    if char.isalpha():
        alpha_chars.append(char)
    elif char.isdigit():
        number_chars.append(char)
    
alpha_chars.sort()
number_chars.sort()

result = ''.join(alpha_chars)+''.join(number_chars)

print(result)