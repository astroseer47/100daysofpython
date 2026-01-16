print("Welcome to Silent Auction")

max_bid = 0
bid_winner = ''
while True:
   choice = str(input("Would you like to bid ?"))
   if choice == "no":
       break
   name = str(input("What is your name?"))
   bid_price = int(input("What is your bid price?"))
   if max_bid < bid_price:
       max_bid = bid_price
       bid_winner = name

print(f"Bidding Ended! Winner is {bid_winner} with bid of {max_bid}" )
