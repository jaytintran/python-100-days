import random
from art import logo

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10]
user_cards = []
computer_cards = []
continue_game = True

def deal_card(list):
  dealt_card = random.choice(cards)
  list.append(dealt_card)

def calc_score(cards):
  for card in cards:
    if card == 10 and card == 11:
      return 0;
    if sum(cards) > 21 and card == 11:
      card = 1
  return sum(cards)

def compare_score(user_score, computer_score):
  if user_score == computer_score:
    print(f"IT'S A DRAW. Your score: {user_score} vs. computer: {computer_cards, computer_score}")
  elif computer_score == 0:
    print(f"GAME OVER, COMPUTER WIN. Your score: {user_score} vs. computer: {computer_cards, computer_score}")
  elif user_score > 21:
    print(f"GAME OVER, COMPUTER WIN. Your score: {user_score} vs. computer: {computer_cards, computer_score}")
  elif user_score == 0:
    print(f"BLACKJACK! You won! Tour score: {user_score} vs. computer: {computer_cards, computer_score}")
  elif user_score > computer_score and user_score < 21:
    print(f"You won! Your score: {user_score} vs. computer: {computer_cards, computer_score}")
  else:
    print(f"You lose! Your score: {user_score} vs. computer: {computer_cards, computer_score}")

# Start the deal
for i in range(0, 2):
  deal_card(user_cards)
  deal_card(computer_cards)

while continue_game == True:
  user_score = calc_score(user_cards)
  computer_score = calc_score(computer_cards)
  if computer_score < 17:
    deal_card(computer_cards)
  if user_score > 21:
    print(f"GAME OVER, COMPUTER WIN. Your score: {user_score} vs. computer: {computer_cards, computer_score}")
    break

  print(f"You have: {user_cards} and your current score is: {user_score}.")
  print(f"First card of the computer is: {computer_cards[0]}")

  continue_draw = input("Do you want to draw another card? Type 'yes' or 'no': ").lower()
  if continue_draw == 'yes':
    deal_card(user_cards)
    user_score = calc_score(user_cards)
    computer_score = calc_score(computer_cards)
    # compare_score(user_score, computer_score)
  elif continue_draw == 'no':
    compare_score(user_score, computer_score)
    continue_game = False
  
  
