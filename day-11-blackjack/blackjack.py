import os
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
first_game = True

def clear_screen():
  os.system('cls||clear')

def draw_logo():
  print(logo)

def offer_instructions():
  instructions = """
    - The deck is unlimited in size. 
    - There are no jokers. 
    - The Jack/Queen/King all count as 10.
    - The the Ace can count as 11 or 1.
    - The following list is the deck of cards:
        [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    - The cards in the list have equal probability of being drawn.
    - Cards are not removed from the deck as they are drawn.
    - The computer is the dealer.
    - The dealer doesn't know your score until after it takes its turn.
    - The dealer must draw if they have less than 17 points and you are not bust.
    - A blackjack (ace and 10) is an automatic win.  
    - If both player and dealer have blackjack, the dealer wins.\n"""

  accepted = input("Would you like to see the houes rules?  y or n: ").lower()
  if accepted == "y":
    print(instructions)

def deal_initial():
  """Returns the starting hands for the game in the form of a dictionary"""
  player_cards = [random.choice(cards) for card in range(2)]

  computer_cards = [random.choice(cards) for card in range(2)]
  hands = {
    "player": player_cards,
    "computer": computer_cards,
  }
  display_hands(hands)
  return hands

def determine_score(hands, user):
  cards = hands[user]
  score = sum(cards)
  if score > 21:
    cards = [1 if card == 11 else card for card in cards]
    hands[user] = cards
    score = sum(cards)
  return (hands, score)

def display_hands(hands):
  player_cards = (", ").join([str(card) for card in hands["player"]])
  hands, player_score = determine_score(hands, "player")
  displayed_computer_card = hands["computer"][0]
  print(f"\nYour cards are: {player_cards}")
  print(f"Your score is: {player_score}")
  print(f"The computer's cards are {displayed_computer_card}, {', '.join(['X' for card in range(len(hands['computer']) - 1)])}\n")

def display_final_results(hands):
  player_cards = (", ").join([str(card) for card in hands["player"]])
  computer_cards = (", ").join([str(card) for card in hands["computer"]])
  hands, player_score = determine_score(hands, "player")
  hands, computer_score = determine_score(hands, "computer")  
  print(f"\nYour final cards are: {player_cards}")
  print(f"Your score is: {player_score}")
  print(f"Computer final cards are: {computer_cards}")
  print(f"Computer score is: {computer_score}")

def player_turn(hands):
  draw_again = input("Draw another card?  y or n: ").lower()
  while draw_again == "y":
    hands["player"].append(random.choice(cards))
    display_hands(hands)
    hands, player_score = determine_score(hands, "player")
    if player_score > 21:
      print("Busted!")
      return hands
    draw_again = input("Draw another card?  y or n: ").lower()
  return hands

def computer_turn(hands):
  hands, player_score = determine_score(hands, "player")
  if player_score > 21:
    return hands
  else:
    print("\nThe computer is taking its turn.")
    hands, computer_score = determine_score(hands, "computer")
    while computer_score < 17:
      computer_cards = (", ").join([str(card) for card in hands["computer"]])
      print(f"The computer's cards are: {computer_cards}")
      print("The computer draws...")
      hands["computer"].append(random.choice(cards))
      hands, computer_score = determine_score(hands, "computer")
  return hands

def determine_winner(hands):
  hands, player_score = determine_score(hands, "player")
  hands, computer_score = determine_score(hands, "computer")

  if player_score > 21 and computer_score > 21:
    return("draw")
  elif player_score > 21:
    return("computer")
  elif computer_score > 21:
    return("player")
  elif player_score == computer_score:
    return("draw")
  elif player_score > computer_score:
    return("player")
  else:
    return("computer")

def print_winner(winner):
  if winner == "draw":
    print("\nIt's a draw.")
  elif winner == "player":
    print("\nYou win!")
  else:
    print("\nYou lose!")

def play_again():
  again = input("\nWould you like to play again?  y or n: ").lower()
  if again == "y":
    start_game()

def blackjack_present(hands):
  if (sum(hands["computer"]) == 21) or (sum(hands["player"])) == 21:
    return True
  else:
    return False

def determine_blackjack_winner(hands):
  if sum(hands["computer"]) == 21:
    print("Computer has a blackjack!  They win!")
    return "computer"
  else:
    print("Player has a blackjack!")
    return "player"

def start_game():
  global first_game
  clear_screen()
  draw_logo()
  if first_game == True:
    offer_instructions()
  first_game = False
  hands = deal_initial()
  if not blackjack_present(hands):
    hands = player_turn(hands)
    hands = computer_turn(hands)
    winner = determine_winner(hands)
  else:
    winner = determine_blackjack_winner(hands)
  display_final_results(hands)
  print_winner(winner)
  play_again()

start_game()
