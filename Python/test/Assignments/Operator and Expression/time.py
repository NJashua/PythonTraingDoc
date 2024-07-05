# 5. Write a program that accepts seconds from keyboard as integer. Your program should converts seconds in hours, minutes and seconds. Your output should like this :

# Enter seconds: 13400
# Hours: 3
# Minutes: 43
# Seconds: 20  

def get_time(seconds):
    hours = seconds//3600 # // for rounding number...:)
    remainint_sec = seconds%3600
    minutes = remainint_sec//60
    seconds = remainint_sec%60
    return hours, minutes, seconds
seconds_value = int(input("Enter seconds Alexa: "))
hours, minutes, seconds = get_time(seconds_value)
print("hours: ",hours)
print("minutes: ",minutes)
print("seconds: ",seconds)
print("")