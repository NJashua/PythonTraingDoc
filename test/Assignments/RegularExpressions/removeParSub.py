import re 

def remove_parenthesis():
    string_val = input("Enter input string: ")
    result = re.sub(r'\s*\([^)]*\)', "", string_val)
    if result:
        print(result)
    else:
        print("Hey")

remove_parenthesis()
