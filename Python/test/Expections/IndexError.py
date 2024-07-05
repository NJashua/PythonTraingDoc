def get_error(list_a, user_val):
    try:
        value = list_a[user_val] 
        return value
    except IndexError as e:
        print(e)
        raise IndexError("Index out of range")  


try:
    list_a = [1,2,4,5]
    user_val = int(input("Enter index val: "))
    data = get_error(list_a, user_val)
    print(data)
except IndexError as e:
    print(e)
    print("Give correct index num man based on list size")