from art import logo, vs
from game_data import data
import random
import os

def clear():
  """Clear console function"""
  # For Windows
  if os.name == 'nt':
      os.system('cls')
  # For macOS and Linux
  else:
      os.system('clear')


def pick_celeb():
  """This function will pick a random celebrety from
  the list of celebrities and return their personal
  attributes along with their follower count"""
  celeb = random.choices(data, k=1)
  name = celeb[0]["name"]
  num_followers = celeb[0]["follower_count"]
  description = celeb[0]["description"]
  country = celeb[0]["country"]
  return name, description, country, num_followers

def check_winner(celebA, celebB):
  if celebA[3] > celebB[3]:
    return "a"
  else:
    return "b"
  

def game():
  print(logo)
  score = 0
  celeb_1 = pick_celeb()
  celeb_2 = pick_celeb()
  
  flag = True
  while flag == True:
    print(f"Compare A: {celeb_1[0]}, a {celeb_1[1]}, from {celeb_1[2]}")
    print(vs)
    print(f"Against B: {celeb_2[0]}, a {celeb_2[1]}, from {celeb_2[2]}")

    guess = input("Who has more followers? Type 'A' or 'B' ").lower()
    clear()
    print(logo)
    
    answer = check_winner(celeb_1, celeb_2)
    
    if guess == answer:
      score +=1
      print(f"Your right! Current score: {score}.")
      celeb_1 = celeb_2
      celeb_2 = pick_celeb()
    else:
      print(f"Sorry that's wrong. Final score: {score}")
      flag = False
game()