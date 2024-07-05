import re 

def lowercase_with_underscore():
    enter_string = input("Enter input string: ")
    result = re.findall(r'[A-Z][a-z]*',enter_string)
    for data in result:
        print(data)

lowercase_with_underscore()
