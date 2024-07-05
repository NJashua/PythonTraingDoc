#4. Write a program that rotates the element of a list so that the element at the first index moves to the second index, the element in the second index moves to the third index, etc., and the element in the last index moves to the first index.

#Soldiers rotate your string.....()()()

string_value = eval(input("Enter a list buhahaha..:"))
result = string_value[-1:]+string_value[:-1] #getting last element first and remaining elements in last buhahaha...:)
print("Original list: ", string_value)
print("Rotated list: ", result)
