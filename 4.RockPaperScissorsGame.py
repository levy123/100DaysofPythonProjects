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
from numpy.random import randint
choice = randint(0,3)
user_choice = (input("Rock Paper or Scissors?")).lower()

if choice == 0:
  print("Computer")
  print(rock)
  if user_choice == "rock":
    print("you")
    print(rock)
    print("Its a tie")
  elif user_choice == "paper":
    print("you")
    print(paper)
    print("You win")
  elif user_choice == "scissors":
    print("you")
    print(scissors)
    print("I win")
  
  
if choice == 1:
  print("Computer")
  print(paper)
  if user_choice == "rock":
    print("you")
    print(rock)
    print("I win")
  elif user_choice == "paper":
    print("you")
    print(paper)
    print("It's a tie")
  elif user_choice == "scissors":
    print("you")
    print(scissors)
    print("You win")

if choice == 2:
  print("Computer")
  print(scissors)
  if user_choice == "rock":
    print("you")
    print(rock)
    print("You win")
  elif user_choice == "paper":
    print("you")
    print(paper)
    print("I win")
  elif user_choice == "scissors":
    print("you")
    print(scissors)
    print("It's a tie")