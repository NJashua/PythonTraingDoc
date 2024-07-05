# 5)write a program to remove duplicate characters from the given string
#   Ex: ABCDABBCDABBBCCDDEEEF
#      output: ABCDEF

value = input("enter sentence: ").upper()
j = []
for i in value:
    if i not in j:
        j.append(i)

result = ''.join(j)
print("Updated String is: ",result)