import random
from game_data import data

def format_data(account):
    return f"{account['name']}"

score = 0
is_game_over = False
random_entry_a = random.choice(data)
random_entry_b = random.choice(data)

while not is_game_over:

    if random_entry_a == random_entry_b:
        random_entry_a = random.choice(data)

    print(f"Compare A : {format_data(random_entry_a)}.")
    print("      -VS-")
    print(f"Compare B : {format_data(random_entry_b)}.")


    guess = str(input("Who has more followers? 'A' or 'B'")).lower()

    a_follower_count = random_entry_a['followers_count']
    b_follower_count = random_entry_b['followers_count']



    if guess == "a" and a_follower_count > b_follower_count:
        score += 1
    elif guess == "b" and b_follower_count > a_follower_count:
        score += 1
    else:
        print(f"Wrong answer, try again. Your final score is {score}")
        break
    print(f"Your Score so far : {score}")
    random_entry_a = random_entry_b
    random_entry_b = random.choice(data)




