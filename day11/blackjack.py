import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10]

print("Welcome to Blackjack!")


def calculate_score(card_deal):
    if sum(card_deal) == 21 and len(card_deal) == 2:
        return 0
    if 11 in card_deal and sum(card_deal) == 21:
        card_deal.remove(11)
        card_deal.append(1)
    return sum(card_deal)

def compare(u_score, d_score):
    if u_score == d_score:
        return "Draw!"
    elif d_score == 0:
        return "Lose, Dealer has Blackjack!"
    elif u_score == 0:
        return "Win with a blackjack!"
    elif u_score > 21:
        return "You went over, you lose!"
    elif d_score > 21:
        return "Dealer went over, you wint!"
    elif u_score > d_score:
        return "You Win!"
    else:
        return "You lose!"
user_deal = [random.choice(cards), random.choice(cards)]
dealer_deal = [random.choice(cards), random.choice(cards)]
dealer_score = -1
user_score = -1
is_game_over = False

while not is_game_over:
    user_score = calculate_score(user_deal)
    dealer_score = calculate_score(dealer_deal)
    print(f"Your cards: {user_deal}, current score: {user_score}")
    print(f"Dealer's first card: {dealer_deal[0]}")
    if user_score == 0  or dealer_score == 0 or user_score > 21:
        print("Game Over!. Dealer Wins")
        is_game_over = True
    else:
        deal_another_card = input("Type 'y' to get another card, type 'n; to pass")
        if deal_another_card == 'y':
            user_deal.append(random.choice(cards))
        else:
            is_game_over = True
            print("Game Over!. Dealer Wins")

while dealer_score != 0 and dealer_score < 17:
    dealer_deal.append(random.choice(cards))
    dealer_score = calculate_score(dealer_deal)

print(compare(user_score, dealer_score))