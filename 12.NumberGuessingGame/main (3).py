#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random


def number_guessing_game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

  #Choose a random number between 1 and 100
  number = random.randint(1,100)
  print(f"Pssst the number is {number}.")

  #Set the difficulty and therefore number of turns
  difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ")
  if difficulty == "hard":
    num_attempts = 5
  else:
    num_attempts = 10

  #Allow the user to make multiple guesses but stop when the user has less than 0 guesses.
  while num_attempts != -1:
    print(f"You have {num_attempts} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    if guess == number:
      print(f"You got it! The answer was {number}")
      break
    elif guess > number:
      print("Too high.\nGuess again")
      num_attempts -=1
    elif guess < number:
      print("Too low.\nGuess again")
      num_attempts -=1
      if num_attempts == 0:
        print("You've run out of guess. You lose.")
        break

number_guessing_game()