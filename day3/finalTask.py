print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("Do you want to go left or right ?")
if direction == "right":
    print("Game Over, you fell into a well")
else:
    action = input("Do you want to swim or wait?")
    if action == "swim":
        print("Game over, you were eaten by a shark.")
    else:
        door = input("Do you wish to go through left door or right door ?")
        if door == "right":
            print("Game Over, you lost the treasure.")
        else:
            print("Great! You found the treasure.")
