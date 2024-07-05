# 2)Write a program to read 6 numbers and create a dictionary having keys EVEN and ODD. Dictionary's value should be stored in list. Your dictionary should be like:
# {'EVEN':[8,10,64], 'ODD':[1,5,9]}

number = int(input("Enter a valid number: "))
even = []
odd = []

result_dict = {"Even": 0, "Odd":0}
for i in range(number):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
result_dict = {}
result_dict['Even'] = even
result_dict['Odd']=odd
print(result_dict)