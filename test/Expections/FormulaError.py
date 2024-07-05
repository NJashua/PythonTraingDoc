class FormulaError(Exception):
    pass

def get_result(user_val):
    try:
        split_operation = user_val.split()
        if len(split_operation) != 3:
            raise FormulaError("Incorrect number of elements in the operation why nake yendhuku ilaaa")

        operand1 = float(split_operation[0])
        operator = split_operation[1]
        operand2 = float(split_operation[2])

        if operator not in ['+', '-', '*', '/']:
            raise FormulaError("Invalid operator.use this operators only bro'+', '-', '*', '/'")

        result = None
        if operator == '+':
            result = operand1 + operand2
        elif operator == '-':
            result = operand1 - operand2
        elif operator == '*':
            result = operand1 * operand2
        elif operator == '/':
            if operand2 == 0:
                raise FormulaError("Division by zero is not allowed ani telusu kadha bro")
            result = operand1 / operand2

        print(f"{user_val} = {result}")
        return result

    except ValueError:
        raise FormulaError("Invalid operand bro.")
    except IndexError:
        raise FormulaError("Invalid input format. use space bro like 2 + 3")
    except FormulaError as e:
        raise e
try:
    user_val = input("Enter operation (e.g: 2 + 3): ")
    data = get_result(user_val)
    print("Operation result is:", data)
except FormulaError as e:
    print(f"FormulaError: {e}")
except Exception as e:
    print(f"Unexpected error occurred: {e}")
