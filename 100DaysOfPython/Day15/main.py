from data import menu
from data import resources


def resource_update(order):
    """Updates the amount of resources left"""
    for item in resources:
        resources[item] -= menu[order]["ingredients"][item]


def resource_check(order):
    """Checks if there are enough resources in the machine"""
    for item in resources:
        if resources[item] < menu[order]["ingredients"][item]:
            return False
    return True


def process_coins(order, coin_payment):
    cost = menu[order]["cost"]
    if coin_payment < cost:
        return False
    elif coin_payment >= cost:
        return True


def money_check(order):
    return menu[order]["cost"]


def report(money):
    return f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee {resources['coffee']}ml \nMoney: ${money}"


total_money = 0
run_machine = True
while run_machine:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "off":
        run_machine = False
    elif user_input == "report":
        print(report(total_money))
    elif resource_check(user_input):
        coins_list = ["quarters", "dimes", "nickles", "pennies"]
        print("Please insert coins.")
        coin_input = [0, 0, 0, 0]
        for count, item in enumerate(coins_list):
            coin_input[count] = int(input(f"How many {item}?: "))
        payment = coin_input[0] * 0.25 + coin_input[1] * 0.1 + coin_input[2] * 0.05 + coin_input[3] * 0.01
        order_cost = menu[user_input]["cost"]
        if process_coins(user_input, payment):
            if payment > order_cost:
                refund = round(payment - order_cost, 2)
                print(f"Here is your change ${refund}")
            resource_update(user_input)
            total_money += order_cost
            print(f"Enjoy your {user_input}! ☕")
        else:
            print("Sorry not enough change. Money refunded. ")
            run_machine = False

