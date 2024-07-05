# 2)write a program to print characters at Odd position and even position for the given string.

string_a = input("enter input string: ")
# 2 position
for i in range(len(string_a)):
    if i%2==0:
        print('even positons are: ', string_a[i])
    else:
        print('odd positions are: ', string_a[i])
