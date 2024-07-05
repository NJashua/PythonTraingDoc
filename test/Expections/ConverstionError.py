def get_result(user_list):
    try:
        split_list = user_list.split(",")
        list_int = []
        for i in split_list:
            convert_int = int(i.strip())
            list_int.append(convert_int)

        return list_int
    except ValueError as janson:
        print(janson)
        print("Give data dam")

try:
    user_list = input("Enter a valid list man: ")
    result = get_result(user_list)
    print(result)
except Exception as ramam:
    print(ramam)
    print("Enter correct list values beta...:)")
