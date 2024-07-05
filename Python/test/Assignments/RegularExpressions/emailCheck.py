# import re 

# count = 0
# pattern = re.compile("james")
# matcher = pattern.finditer("ababababababjamesjamesjamesjamesss")
# for match in matcher:
#     count += 1

# print(count)

# full match...

# import re 

# user_input = input("enter user val: ")

# pattern = re.fullmatch(user_input, "Hey Nithin Jashua")

# if pattern:
#     print(" Hey match end is",pattern.start())
# else:
#     print("No match found")

#  searching...

# import re 
# u_val = "Hey"
# value = "Hey Nithin Jashua"
# pattern = re.search(u_val, value)

# if pattern:
#     print("Hey you found match", pattern.group())

# import re
# list_a = re.findall("[0-9]","a2feb4nj4 45in 4")
# print(list_a)



# import re
# list_a = "who hey hi james cam hello nithin jashua, hames afien feni"
# result = re.split('\s', list_a,1)
# print(result)
# import re 
# list_a = re.sub('[a-z]',"$" ,"af4r48yfkw4r8y49fb48yr", 2) # we can add the count also like (cond, sub char, txt, count)
# print(list_a)
# if list_a != None:
#     for i in list_a:
#         value = i.group()
#         value_j = i.end()
#         print("Hey you found match", value)
#         # print("Second match", value_j)


# import re as james

# text_data = "hey james cam where is avatar series"

# result = james.search(r"\bs\w+", text_data)
# print(result)

# import re

# txt = "The rain in spain"
# x = re.search(r"\bS\w+", txt)
# print(x.string())

# import re

# txt = "The rain in india"
# x = re.search("India", txt, re.IGNORECASE)

# if x != None:
#     print("text ends with india")

# import re

# num = input("Enter mobile number: ")

# is_match = re.fullmatch("[6789][0-9][0-9]", num)

# if is_match != None:
#     print("Hey match!!!")
# else:
#     print("Give correct number")

# import re 
# import urllib
# import urllib.request

# url_data = urllib.request.urlopen("https://www.redbus.in/info/contactus")
# text_data = url_data.read()
# result = re.findall("[0-9]{12}", str(text_data)) #r'\b\d{12}\b
# for i in result:
#     print(i)

# https://www.rediff.com/

# import re 
# import urllib
# import urllib.request

# url_data = urllib.request.urlopen("https://www.rediff.com/")
# text_data = url_data.read()
# result = re.findall("<title>.*</title>", str(text_data)) #r'\b\d{12}\b
# print(result)

# for number in result:
#     print(number)

import re

def check_email_valid():
    email = input("Enter email: ")
    result = re.match(r"^[a-zA-Z0-9.]+@gmail\.com$", email) 
    if result != None:
        print("Email is valid")
    else:
        print("Invalid email id, give correct email")

check_email_valid()
