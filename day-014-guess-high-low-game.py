from art import logo_guess_high_low 
from game_data import data
import random

print("Welcome to Higher Lower Game")
print(logo_guess_high_low)

# Print the description and stats of the person
def printStat(person):
  name = person["name"]
  description = person["description"]
  country = person["country"]
  return f"{name} is a {description} from {country}."

# Get two random person from the database
def getData(data):
  i = random.randint(0, len(data) - 1)
  return data[i]

# Check answer
def checkAnswer(guess, person1_followers, person2_followers):
  if person1_followers > person2_followers:
    return guess == 'a'
  else:
    return guess == 'b'

# Game
def startGame():
  score = 0
  should_contine = True
  person1 = getData(data)
  person2 = getData(data)
  while should_contine == True:
    person1 = person2
    person2 = getData(data)
    # Get the number of followers from each person
    person1_followers = person1['follower_count']
    person2_followers = person2['follower_count']

      # Display the stats of the two person
    print(f"Compare A: {printStat(person1)}.")
    print('vs.')
    print(f"Against B: {printStat(person2)}.")
      
    # Ask user for input on which person they choose
    answer = input("Which person has more followers on Instagram? Type A or B: ").lower()
  
    is_correct = checkAnswer(answer, person1_followers, person2_followers)
    print(logo_guess_high_low)
    if is_correct:
      score += 1
      print(f"Yes you won! Your score is {score}.")
      person1 = person2
    else:
      print(f"No you lose. Your score is {score}.")
      should_contine = False


  # # Compare two generated person's follower number and the player's answer
  # if answer == 'a':
  #   answer = person1_followers
  #   if (answer > person2_followers):
  #     print(f"Yes you won! Your choice is {person1['name']} and he/she has {person1['follower_count']} million of followers on Instagram.")
  #   elif (answer < person2_followers):
  #     print(f"No you lose!\nYour choice is {person1['name']} and he/she has {person1['follower_count']} million of followers on Instagram.\nvs.\n{person2['name']} and he/she has {person2['follower_count']} million of followers on Instagram.")
  # elif answer == 'b':
  #   answer = person2_followers
  #   if (answer > person1_followers):
  #     print(f"Yes you won! Your choice is {person2['name']} and he/she has {person2['follower_count']} million of followers on Instagram.")
  #   elif (answer < person1_followers):
  #     print(f"No you lose!\nYour choice is {person2['name']} and he/she has {person2['follower_count']} million of followers on Instagram.\nvs.\n{person1['name']} and he/she has {person1['follower_count']} million of followers on Instagram.")
  # else:
  #   print("Invalid input.")


startGame()

# for number in range(0, 2):
#   i = random.randint(0, len(data))
#   print(data[i])

# print(data[i]['follower_count'])

