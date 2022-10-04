
logo = """
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""

print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Create dictionary: keys are math operations and values are the name of the function

operands = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    num1 = float(input("What's the first number? \n"))

    for operand in operands:
        print(operand)

    should_continue = True

    while should_continue:
        chosen_operand = input("Which operation do you want? \n")
        num2 = float(input("What's the next number? \n"))
        calculation_function = operands[chosen_operand]
        answer = calculation_function(num1, num2)

        print(f"The result is {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation \n") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
