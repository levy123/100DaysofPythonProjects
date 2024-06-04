from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

def silent_auction():
  print(logo)
  print("Welcome to the secret auction program")
  flag = True
  auction_log = []
  while flag == True:
    user_name = input("What is your name?: ")
    bid_value = int(input("What is your bid?: "))
    to_repeat = input("Are there any other bidders? Type 'Yes' or 'No'. ").lower()
    auction_entry = {}
    auction_entry["name"] = user_name
    auction_entry["bid"] = bid_value
    auction_log.append(auction_entry)
    def find_highest_bidder(auction_log):
      highest_bid = 0
      for bidder in auction_log:
        if bidder["bid"] > highest_bid:
          highest_bid = bidder["bid"]
          highest_bidder = bidder["name"]
      print("Congratulations", highest_bidder, "You are the winner with", highest_bid)
      
    if to_repeat == "no":
      flag = False
      find_highest_bidder(auction_log)
    else:
      clear()

silent_auction()
  


    

