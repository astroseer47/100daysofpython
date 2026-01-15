# Function with inputs

# name is parameter
# John (value) is argument
def greet(name):
    print(f"Hello {name}!")

greet("John")


# Function with more than 1 input

def greet(name, city):
    print(f"Hello {name} from {city}!")

greet("John", "San Diego")
greet(city="Man", name="Jane")