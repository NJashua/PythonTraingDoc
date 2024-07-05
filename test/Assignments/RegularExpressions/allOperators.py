import re 

def match_all_char():
    enter_str = input("Enter a string: ")
    result = re.findall(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*_)', enter_str)
    if result:
        print("Match one")
    else:
        print("Un-matched")
match_all_char()