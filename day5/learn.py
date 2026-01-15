# Loops

# For Loop

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


scores = [11,1234,41,34,122,55,12]
print(sum(scores))

total = 0
max_score = 0
for score in scores:
    total += score
    if score > max_score:
        max_score = score

print(total)

print(max(scores))
print(max_score)


# For Loop - Range

total_sum = 0
for number in range(1,101):
    total_sum += number

print(total_sum)