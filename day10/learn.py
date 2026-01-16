# Functions with outputs

def my_function(param):
    # Do something
    return 0

def sum():
    result = 3 * 9
    return result

print(sum())


def format_greeting(user_details):
    """Prepare a greeting message
    with user's name and city"""
    greeting = "Hello " + user_details["name"] + " from " + user_details["city"]
    return greeting


user_details = {"name": "John", "city": "KL"}
print(format_greeting(user_details))