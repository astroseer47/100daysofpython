import random

print("Rock, Paper, Scissors")
options = ['Rock', 'Paper', 'Scissors']
users_choice = input("What do you choose?")
computers_choice = random.choice(options)
print(f"Your choice {users_choice}")
print(f"Computer's choice {computers_choice}")

if users_choice == computers_choice:
    print("It's a draw")
elif users_choice == 'Rock' and (computers_choice == 'Paper' or computers_choice == 'Scissors'):
    print("User Wins")
elif users_choice == 'Paper' and (computers_choice == 'Rock'):
    print("User Wins")
elif users_choice == 'Scissors' and computers_choice == 'Paper':
    print("User Wins")
else:
    print("Computer Wins")

