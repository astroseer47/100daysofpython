import random
print("Welcome to the Guess Number game!")

print("I am thinking of a number between 1 and 100")

number = random.randint(1,100)

num_of_guesses = 10
choice = str(input("Choose a difficulty level : 'easy' or 'hard'"))

if choice == 'hard':
    num_of_guesses = 5

is_game_over = False

while not is_game_over:
    guess = int(input(f"You have {num_of_guesses} attempts. Make a guess: "))
    num_of_guesses -= 1
    if guess == number:
        print(f"You guessed it right! {number}")
        break
    if guess < number:
        print("Your guess is too low. Guess again!")
    else:
        print("Your guess is too high. Guess again!")

    if num_of_guesses == 0:
        print("You lose!")
        break

