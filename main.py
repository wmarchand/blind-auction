from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo + "\nWelcome to the secret auction program.")

auctions = {}

more_auctions = True
while more_auctions:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    auctions[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes or 'no'. ").lower()
    
    if other_bidders == "no":
        more_auctions = False
    elif other_bidders == "yes":
        clear()
    else:
        other_bidders = input("Are there any other bidders? Type 'yes or 'no'. ").lower()
auction_winner = ""
bid_winner = 0
for key in auctions:
    if auctions[key] > bid_winner:
        bid_winner = auctions[key]
        auction_winner = key
        
print(f"The winner is {auction_winner} with a bid of ${bid_winner}.")