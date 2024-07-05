def get_result(*args):
    value = []
    try:
        value.append(sum(args))
    except:
        print("Getting error")
    finally:
        print("result is: ")
        return value
try:
    result = get_result(1, 4)
    print(result)
except:
    print("Bye")