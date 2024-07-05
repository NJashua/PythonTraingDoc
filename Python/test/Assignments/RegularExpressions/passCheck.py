import re 

def check_password():
    enter_pass = input("Enter password: ")
    result = re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d{8})[a-zA-Z0-9]{10,}$", enter_pass) #google it r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d{8})[a-zA-Z0-9]{10,}$"
    if result != None:
        print("Password valid")
    else:
        print("Password is not valid")
    

check_password()