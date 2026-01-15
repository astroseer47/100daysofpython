import random

countOfOne = 0
countOfTwo = 0

counter = 0

while counter < 10000:
    randInt = random.randint(1, 2)
    if randInt == 1:
        countOfOne += 1
    else:
        countOfTwo += 1
    counter += 1

print(f"Count of 1 {countOfOne} and count of 2 {countOfTwo}")

