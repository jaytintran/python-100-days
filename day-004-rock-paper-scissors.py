rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

user_choice = str(input("Rock, Paper or Scissor? Type in..."))

computer_choice = random.randint(1, 4)
print(computer_choice)

if computer_choice == 1:
    print(rock)
elif computer_choice == 2:
    print(paper)
else:
    print(scissors)
