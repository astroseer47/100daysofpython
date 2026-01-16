print("Welcome to calculator!")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiple(a, b):
    return a * b

def divide(a, b):
    return a / b

operators = {
    "add": add,
    "subtract": subtract,
    "multiply": multiple,
    "divide": divide
}

print(operators)

should_continue = True
while should_continue:
    num1 = int(input("What's the first number ?"))
    operator = str(input("What's the operator ? add, subtract, multiply, divide ?"))
    num2 = int(input("What's the second number ?"))
    result = operators[operator](num1, num2)
    print(f"Result is {result}")
    choice = input("Would you like to continue ? (y/n)")
    if choice == "n":
        should_continue = False

