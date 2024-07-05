def perform_operation(operation, a, b):
    try:
        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '*':
            return a * b
        elif operation == '/':
            return a / b
        else:
            raise ValueError("Invalid operation")
    except AttributeError as e:
        print(f"AttributeError: {e}")
        print("Check if the operands are of correct type or not bro.")
    except ValueError as e:
        print(f"ValueError: {e}")
        print("give valid operation in this man '+', '-', '*', '/'.")

try:
    a = int(input("Enter a value for a: "))
    b = int(input("Enter a value for b: "))
    operation = input("Enter an operation (+, -, *, /): ")

    result = perform_operation(operation, a, b)
    if result is not None:
        print(f"Result of {a} {operation} {b} is: {result}")
except ValueError as e:
    print(f"ValueError: {e}")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
