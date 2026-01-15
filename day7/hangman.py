import random

word_list = ["hello", "magic", "education", "mouse", "river", "sunshine"]

word = random.choice(word_list)

guessed_letters = []

lives = 5
is_saved = False
while lives > 0:
    guessed_letter = input("Guess the letter : ")
    if guessed_letter in word:
        guessed_letters.append(guessed_letter)
        if len(guessed_letters) == len(word):
            is_saved = True
            break
    else:
        print("The letter you guessed is wrong, you lose a life!")
        lives -= 1

if is_saved:
    print(f"You guessed it right. Its {word}")
else:
    print("Uh oh! You lose!")

