def get_table(n):
    table = []
    for i in range(1, 11):
        value = f"{n} X {i} = {n*i}"
        table.append(value)
    return table
number = int(input("Enter a number: "))
value = get_table(number)
print(f"Table for {number} is: ")
for i in value:
    print(i)

