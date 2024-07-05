list_a = list(input("Enter a list of items: ").split(',')) #[10,20,30,40,50,60]#input("Enter a list of items: ") removing the comma and splitting into a list...:)
result = list_a[::2]
for i in result:
    print("Alternate elements are: ", i)