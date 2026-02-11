# Errors: FileNotFound,  KeyError, IndexError, TypeError, ValueError


# FileNotFound error
# with open("somefile,txt") as file:
#     file.read()

try:
    with open("somefile,txt") as file:
        file.read()
except FileNotFoundError:
    print("File not found")

# Throwing Error
raise KeyError

