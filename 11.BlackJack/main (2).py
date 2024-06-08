############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

from art import logo
import random

print(logo)

#create function to calculate current score
def current_score(u_cards, c_cards):
  """Take a list of cards and return the score
  and print a message to the console"""
  u_score = sum(u_cards)
  c_score = sum(c_cards)
  #display the users cards and current score
  print(f"Your cards: {u_cards}, current score: {u_score}")
  #display the computer's first card
  print(f"Computer's first card: {c_cards[0]}")
  return u_score, c_score

#create function to find the player's final scores
def final_score(u_cards, c_cards):
  """Take a list of cards and calculate the final 
  score and print the final scores"""
  u_score = sum(u_cards)
  c_score = sum(c_cards)
  #11 will change to a value of 1 if the player's cards are over 21
  if u_score > 21:
    if 11 in u_cards:
      index = u_cards.index(11)
      u_cards[index] = 1
      u_score = sum(u_cards)
  if c_score > 21:
    if 11 in c_cards:
      index = c_cards.index(11)
      c_cards[index] = 1
      c_score = sum(c_cards)
  #print the final scores
  print(f"Your final hand: {u_cards}, current score: {u_score}")
  print(f"Computer's final hand: {c_cards}, final score: {c_score}")
  return u_score, c_score

#create function to decide the winner
def decide_winner(u_score, c_score):
  """Take the scores and decide the winner
  based on the scores"""
  if u_score == c_score:
    print("You both draw!")
  elif u_score > 21:
    print("You went over. You Lose")
    flag = False
  elif c_score > 21:
    print("You win!")
  elif c_score > u_score:
    print("You Lose!")
  elif u_score > c_score:
    print("You Win!")
  
  
def blackjack():
  """The main BlackJack game"""
  #set of possible cards/scores in the game
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

  #randomly choose 2 cards for the user and computer from the cards list
  user_cards = random.choices(cards, k=2)
  computer_cards = random.choices(cards, k=2)
  
  #calculate the user and computer's scores given the cards
  user_score, computer_score = current_score(user_cards, computer_cards)

  #check if any of the players got Black Jack on the first draw
  if user_score == 21:
    print("You got BlackJack! You win!")
    return
  elif computer_score == 21:
    print("The computer got BlackJack! You Lose!")
    print(f"Computer's hand: {computer_cards}, computer's score {computer_score}")
    return
  #create boolean flag variable
  flag = True
  #main game loop
  while flag == True:
    #ask user if they want to stop or continue playing
    to_continue = input("Type 'y' to get another card, type 'n' to pass: ")
    if to_continue == 'y':
      #add another card for the user
      user_cards.extend(random.choices(cards, k=1))
      #add another card for the computer if the computer's score is >= 13
      if computer_score <= 13:
        computer_cards.extend(random.choices(cards, k=1))
      #get the final scores
      u_final_score, c_final_score = final_score(user_cards, computer_cards)
      #find the winner and end the game
      decide_winner(u_final_score, c_final_score)
      flag = False
    else:
      #print the current scores and end game if player doesn't want to pick another card
      print(f"Computer's hand: {computer_cards}, computer's score {computer_score}")
      decide_winner(user_score, computer_score)
      flag = False
  play_again = input("Do you want to play again? Type 'y' or 'n':")
  if play_again == 'y':
    blackjack()
  else:
    return
blackjack()











#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

