MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 21,
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def print_report():
    print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: ${resources['money']}")

def update_resources(ingredients, price):
    resources['water'] -= ingredients['water']
    resources['milk'] -= ingredients['milk']
    resources['coffee'] -= ingredients['coffee']
    resources['money'] += price



def are_resources_available(s_choice, required_ingredients):
    if required_ingredients['water'] > resources["water"]:
        return False
    if s_choice == 'espresso' and required_ingredients['milk'] > resources["milk"]:
        return False
    if required_ingredients['coffee'] > resources["coffee"]:
        return False

    return True

while True:
    choice = str(input("What would you like ? (espresso/latte/cappuccino):")).lower()
    if not choice in ["espresso", "latte", "cappuccino", "off", "report"]:
        print("Invalid choice")
        continue

    if choice == "off":
        break

    if choice == "report":
        print_report()
        continue
    selected_item = MENU[choice]

    if not are_resources_available(choice, selected_item["ingredients"]):
        print("Sorry, resources are not available")
        continue

    print(f"Great! You have chosen {choice}. Price is ${selected_item['cost']}")

    print("Please insert coins 🪙")
    quarters = int(input("How many quarters? ").strip() or 0) #0.25$
    dimes = int(input("How many dimes? ").strip() or 0) #0.10$
    nickles = int(input("How many nickles? ").strip() or 0) #0.05$
    pennies = int(input("How many pennies? ").strip() or 0) #0.01$

    print(quarters, dimes, nickles, pennies)

    total_inserted_amount = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    print(f"You have inserted a total of ${total_inserted_amount}")

    coffee_price = selected_item["cost"]

    change_to_return = 0
    if total_inserted_amount < coffee_price:
        print(f"Sorry, inserted coins are not sufficient to brew {choice}. Money refunded")
        continue

    if total_inserted_amount > coffee_price:
        change_to_return = total_inserted_amount - coffee_price

    print("Let's start brewing! ☕️")
    update_resources(selected_item["ingredients"], coffee_price)

    print(f"Your {choice} is ready. Dispensing")
    if change_to_return > 0:
        print(f"Here is your ${change_to_return} in change!")

