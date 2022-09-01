#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo_guess_number
EASY_TURNS = 10
HARD_TURNS = 5

def check_answer(guess, answer):
  if guess > answer:
    print("Too high.")
  elif guess < answer:
    print("Too low.")
  elif guess > 100 or guess < 0:
    print("Invalid guess.")
  else:
    print(f"You've got it. The answer is {answer}")

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == 'easy':
    return EASY_TURNS
  elif level == 'hard':
    return HARD_TURNS

def game():
  print(logo_guess_number)
  print("Welcome to Number Guessing Game!")
  print("I'm thinking a number between 1 and 100")
  solution_number = random.randrange(1, 100)
  guess_attempts = set_difficulty()
  
  while not guess_attempts == 0:
    print(f"You have {guess_attempts} guesses remaining left to guess the number.")
    guess = int(input("Make a guess: "))
    check_answer(guess, solution_number)
    guess_attempts -= 1
  
    if guess_attempts == 0:
      print("You've run out of guesses. You lose.")
    elif guess == solution_number:
      break

game()
