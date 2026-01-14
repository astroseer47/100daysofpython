print("Welcom to Python Pizza Deliveries!")
size = input("What size ? S, M or L:")
pepperoni = input("Do you want pepperoni on your pizza ? Y or N:")
extra_cheese = input("Do you eant extra cheese ? Y or N:")

small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_price = 2
extra_cheese_price = 3

total_bill = 0
if size == "S":
    total_bill+= small_pizza
elif size == "M":
    total_bill += medium_pizza
elif size == "L":
    total_bill += large_pizza

if pepperoni == "Y" and size == "S":
    total_bill += 2
elif pepperoni == "Y" and size != "S":
    total_bill += 3


if extra_cheese == "Y":
    total_bill += extra_cheese_price

print(total_bill)