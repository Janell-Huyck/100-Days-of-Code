from replit import clear
from art import logo

print(logo)
bids = {}

def add_new_bid(name,bid):
  global bids
  bids[name] = bid

def get_new_bid():
  name = input("What is your name? ")
  bid = int(input("Please enter your bid: "))
  add_new_bid(name, bid)

def determine_winner(bids):
  winner = ["nobody", 0]
  for name in bids:
    if bids[name] > winner[1]:
      winner[0] = name
      winner[1] = bids[name]
  print(f"The winner is {winner[0]} with a bid of {winner[1]}.")

def auction():
  global bids
  get_new_bid()
  if input("Is there another bidder?  (Type 'yes' or 'no') ").lower() == "yes":
    clear()
    auction()
  else:
    determine_winner(bids)

auction()
