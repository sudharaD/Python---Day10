from replit import clear

# Add
def add(num1, num2):
    return num1 + num2

# Substract
def substract(num1, num2):
    return num1 - num2

# Multiply
def multiply(num1, num2):
    return num1 * num2

# Devide
def devide(num1, num2):
    return num1 / num2

while True:

    operator_list = {
        "+": add,
        "-": substract,
        "*": multiply,
        "/": devide,
    }
    is_continue = True
    first_number = float(input("What is your first number?: "))
    for item in operator_list:
        print(item)

    while is_continue:
        operator = input("Pick an operation: ")
        next_number = float(input("What is the next number?: "))
        # if operator == "+":
        #     result = operator_list[operator](first_number, next_number)
        # elif operator == "-":
        #     result = operator_list[operator](first_number, next_number)
        # elif operator == "*":
        #     result = operator_list[operator](first_number, next_number)
        # else:
        #     result = operator_list[operator](first_number, next_number)
        result = operator_list[operator](first_number, next_number)

        print(f"{first_number} {operator} {next_number} = {result}")
        check_continue_calculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if check_continue_calculation == "n":
            clear()
            is_continue = False

        first_number = result