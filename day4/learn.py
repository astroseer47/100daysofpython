# Randomisation and Lists

#Random Module: import random
import random

print(random.random())
print(random.uniform(10,20))
print(random.randint(1,2))

random_number = random.randint(1,2)
if random_number == 1:
    print("Heads")
else:
    print("Tails")



# List
# - Data structure
# List
fruits = ["apple", "mango", "banana"]
print(fruits)
print(fruits[2])
fruits[2] = "cherry"
print(fruits[2])
fruits.append("orange")
print(fruits)

names = ["John", "Jane", "Albert", "Blake", "Darren"]

print(names[random.randint(0, len(names) - 1)])

print(random.choice(names))

list1 = [1,2,3]
list2 = [4,5,6]
merged =[list1, list2]
print([list1, list2])
print(merged[1][1])