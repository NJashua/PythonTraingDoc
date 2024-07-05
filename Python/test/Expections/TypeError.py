def get_error(a, b):
    try:
        result = a + b
        print("sume of a and b is :", result)
    except TypeError:
        raise TypeError("Give correct values")

try:
    a = int(input("Enter a value for a: "))
    b = int(input("Enter a value for b: "))
    get_error(a, b)
except ValueError as error:
    print(error)
    print("Correct values ivvura ayya")  
except TypeError as e:
    print(e)
