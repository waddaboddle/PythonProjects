import art

print(art.logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    first_number = float(input("What is your first number?: "))
    for symbol in operations:
        print(symbol)
    calc_continue = True

    while calc_continue:
        operator = input("Pick an operation: ")
        second_number = float(input("What is the next number?: "))
        calculation_function = operations[operator]
        total = calculation_function(first_number, second_number)

        print(f"{first_number} {operator} {second_number} = {total}")

        keep_going = input(f"Type 'y' to continue calculating with {total}, or type 'n' to start a new calculation: ")
        if keep_going == "y":
            calc_continue = True
            first_number = total
        else:
            calc_continue = False
            calculator()


calculator()
