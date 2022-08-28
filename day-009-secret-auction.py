from operator import itemgetter
from replit import clear
from art import logo_auction
print("Welcome to Blind Aunction Program")
print(logo_auction)

bidding_finished = False
bid_list = []
while not bidding_finished:
  # Clearing the Screen
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  
  bid_person = {}
  bid_person["name"] = name 
  bid_person["bid_amount"] = bid

  # Add the bidder to the bid list
  bid_list.append(bid_person)

  # Check if there's still other bidders
  other_bidder = input("Are there other bidders? Type \"yes\" or \"no\": ").lower()
  if other_bidder == "no":
    bidding_finished = True
  elif other_bidder == "yes":
    clear()

# Compare each person bid to each other and pick out the highest bid
clear()
highest_bidder = max(bid_list, key=itemgetter('bid_amount'))
print(f"The winner of this auction goes to: {highest_bidder['name']} with the bid of ${highest_bidder['bid_amount']}!!!")