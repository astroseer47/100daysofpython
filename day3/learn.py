# Conditions

answer = False
if answer:
    print("true")
else:
    print("false")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# Operators: > < = ! >= <= == !=
if height >= 120:
    print("You can ride")
    age = int(input('What is your age? '))
    if age >= 26:
        print("Please pay $17")
    elif 22 <= age <= 26:
        print("Please pay $10")
    else:
        print("Please pay $3")

else:
    print("Sorry, you cannot ride")

# Modulo - remainder
print(10 % 2)
print(10  % 3)

print("Welcome to odd / even checker")
number = int(input("Please enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Logical Operators
print(True and True)
print(False or True)
print(False and False)
