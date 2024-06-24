import art

print(art.logo)


def calculate(n1, n2, op):
    if op == "+":
        return n1 + n2
    if op == "-":
        return n1 - n2
    if op == "*":
        return n1 * n2
    if op == "/":
        return n1 / n2


def calculator():
    first_number = float(input("What is your first number?: "))
    print("+ \n- \n* \n/")
    calc_continue = True
    while calc_continue:
        operator = input("Pick an operation: ")
        second_number = float(input("What is the next number?: "))
        total = round(calculate(first_number, second_number, operator), 2)
        print(f"{first_number} {operator} {second_number} = {total}")

        keep_going = input(f"Type 'y' to continue calculating with {total}, or type 'n' to start a new calculation: ")
        if keep_going == "y":
            calc_continue = True
            first_number = total
        else:
            calc_continue = False
            calculator()


calculator()
