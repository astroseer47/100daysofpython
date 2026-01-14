print("Welcome to the tip calculator!\n")
bill = input("What was the total bill ?$")
tip = input("How much tip would you like to give ?")
people = input("How many people split the bill?")

total_tip = float(bill) * (int(tip)/100)

total_bill = float(bill) + total_tip
individual_bill = total_bill / int(people)
print(f"Each person should pay: ${round(individual_bill,2)}")