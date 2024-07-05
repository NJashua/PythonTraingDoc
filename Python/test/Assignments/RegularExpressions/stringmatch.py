import re 


def matching_string():
    string_a = input("Enter a string: ")
    result = re.match(r"^(?=0|b).*$", string_a)
    if result:
        print("String matched")
    else:
        print("String not matched")

matching_string()
