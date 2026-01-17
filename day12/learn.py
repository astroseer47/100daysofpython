# Namespaces: Local vs Global Scopes, Constants

apples = 100

def apples_count():
    global apples
    apples = 22
    print(f"apples count inside function {apples}")

apples_count()
print(f"apples count outside {apples}")

# Global Constants
PI = 3.14159
HOME_URL = "https://www.myhome122"

