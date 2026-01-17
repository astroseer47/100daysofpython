# Debugging
def my_function():
    print("Hello!")

# Function never called




def my_function2():
    for i in range(1,20):
        print(i)
        if i == 20:
            print("Here!")

my_function2()
# range ends at 19, and never reaches 20


# Error Handling : TRY-EXCEPT

try:
    age = int(input("How old are you? "))
except ValueError:
    print("Error!")
    age = int(input("How old are you? "))

if age > 18:
    print("You are old enough to vote!")