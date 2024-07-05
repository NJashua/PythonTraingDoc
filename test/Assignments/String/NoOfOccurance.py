# 6)write a program to find the number of occurrence of each character present in
#   the given string.
#     input : ABBABCDDC
#     output : A-2,B-3,C-2,D-2

# 6 count
data = input("enter sentence: ")

result = {}
for char in data:
    if char in result:
        result[char] += 1
    else:
        result[char] = 1
    
for char, count in result.items():
    print(f"{char} - {count}")