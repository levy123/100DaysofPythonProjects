from game_data import MENU, resources


def output_report():
    """ Prints the current resources available """
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    print(f"""
    Water: {water}m;
    Milk: {milk}ml
    Coffee: {coffee}g
    Money: ${money}
    """)


def check_resources(chosen_drink):
    """ Takes the drink chose by the user and loops through the
    ingredients list comparing the [value] which is the amount
    of each ingredient needed to the available resources in
    the coffee machine """
    flag = True
    for key, value in MENU[chosen_drink]["ingredients"].items():
        amount_left = resources[key] - value
        if amount_left < 0:
            print(f"Sorry there is not enough {key}")
            flag = False
    return flag


def make_drink(chosen_drink):
    """ Takes the chosen drink and makes it, reducing the
    resources available in the machine """
    for key, value in MENU[chosen_drink]["ingredients"].items():
        # Reduce resources of coffee machine based on drink made
        resources[key] -= value
    print(f"Here is your {chosen_drink}. Enjoy!")


def process_coins():
    """ Gets the user to enter their coins and
     adds up the money entered"""
    print("Please insert coins")
    quarters = float(input("How many quarters?: ")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.10
    nickels = float(input("How many nickels?: ")) * 0.05
    pennies = float(input("How many pennies?: ")) * 0.01

    money_entered = round(quarters + dimes + nickels + pennies, 2)
    print(f"Money entered: ${money_entered}")
    return money_entered


def check_transaction(chosen_drink, money_entered):
    """ Checks that the user has inserted enough coins
    to buy the drink and outputs error message if the coins
    are not enough and adds the cost of the drink to
    resources if the coins are enough. It also gives change"""
    flag = True
    cost = MENU[chosen_drink]["cost"]
    if cost > money_entered:
        print("Sorry that's not enough money. Money returned.")
        flag = False
    else:
        change = round(money_entered - cost, 2)
        if change > 0:
            resources["money"] += cost
            print(f"Here is your change: ${change}")
    return flag


def coffee_machine():
    """ The main logic of the coffee machine.
    Allows user to turn the machine off and select a drink"""
    flag = True
    while flag:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice == 'report':
            output_report()
        elif user_choice == 'off':
            flag = False
        else:
            # Catch errors that occur when user enters an invalid choice
            try:
                # Check if there are enough resources to make the drink
                sufficient_resources = check_resources(user_choice)
                if sufficient_resources:
                    # Collect coins
                    user_coins = process_coins()
                    transaction_successful = check_transaction(user_choice, user_coins)
                    # Check if there were enough coins to buy the drink
                    if transaction_successful:
                        make_drink(user_choice)
            except KeyError:
                print("I don't recognise that option. Please try again")


coffee_machine()
