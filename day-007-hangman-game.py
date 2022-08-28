import random
from hangman_words import word_list
from art import hangman_stages
from art import logo_hangman
# word_list = ["aardvark", "baboon", "camel"]
# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
blanks = []
print("Welcome Hangman Game!")
print(logo_hangman)
print(hangman_stages[len(hangman_stages) - 1])

i = 0
while i < len(chosen_word):
  blanks += "_"
  i += 1

print(blanks)

# Looping again and again until user has complete the guessing game
end_game = False
lives = 6
state = len(hangman_stages) - 1
while not end_game:
  # Ask the user to guess then make it lowercase.
  guess = input("\nGuess a letter: ").lower()
  # Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
      blanks[position] = letter
  # If use guesses wrong 
  if guess not in chosen_word:
    state -= 1
    print(hangman_stages[state])
    lives -= 1
    print("You lose 1 live, you have: " + str(lives) + " lives left")
    if lives == 0:
      print("GAME OVER!!!")
      break
  # Check if all blanks has been replaced
  if "_" not in blanks:
    end_game = True
    print("YOU WON!!!")
  print("------------------------------------")
  print(f"{' '.join(blanks)}")

    
# i = 0
# res = ""
# while i < len(chosen_word):
#   if guess == chosen_word[i]:
#     print("true")
#     res += guess
#   elif guess != chosen_word[i]:
#     print("false")
#     res += "_"
#   i += 1
# print(res)



