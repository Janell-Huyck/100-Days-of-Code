import random
import os
from art import logo, vs
from game-data import data

score = 0

def reset_screen():
  os.system('cls||clear')
  print(logo)

def print_instructions():
  print("""
    Higher Lower is a guessing game based on your best guess for
    which of two people or things have more followers on Instagram,
    based off data from 2022.  
    
    You will be shown two options to compare.  They will be labeled 
    as 'A' and 'B'.  Type in either 'A' or 'B', depending on which
    of these two you believe has more IG followers.
    
    If you guess incorrectly, the game ends.  If you guess correctly,
    the game continues.  The option that had been in slot 'B' becomes
    choice 'A', and a new choice is presented for 'B'.  
    
    Continue guessing which has the most IG followers until you guess incorrectly.\n
  """)
  input("Hit enter to continue...")

def start_game():
  reset_screen()
  print_instructions()
  choices = make_initial_choices()
  continue_game(choices)

def make_initial_choices():
  choice_a = {}
  choice_b = {}

  while choice_b == choice_a:
    choice_a = random.choice(data)
    choice_b = random.choice(data)

  choices = {
    "A": choice_a,
    "B": choice_b
  }
  return choices

def choice_is_correct(choices, player_choice):
  higher_count = pick_higher_count(choices)
  
  if player_choice == higher_count:
    return True
  else:
    return False

def pick_higher_count(choices):
  count_a = choices["A"]["follower_count"]
  count_b = choices["B"]["follower_count"]
  
  higher_count = "a" if count_a >= count_b else "b"
  return higher_count

def increase_score():
  global score
  score += 1

def print_choice(choice):
  print(f'{choice["name"]}, a {choice["description"]} from {choice["country"]}')

def get_player_choice(choices):
  reset_screen()
  print(f"Your current score is {score}")
  print("Enter 'help' to print instructions.\n")
  print("Choice A:")
  print_choice(choices["A"])
  print(vs)
  print("Choice B:")
  print_choice(choices["B"])
  player_choice = input("\nWhich has more followers - A or B? ").lower()
  return player_choice

def advance_to_next_question(choices):
  choices = get_next_choice(choices)
  reset_screen()
  return choices

def get_next_choice(choices):
  higher_choice = pick_higher_count(choices).upper()
  new_a = choices[higher_choice]
  new_b = random.choice(data)
  choices = {
    "A": new_a,
    "B": new_b
  }
  return choices

def continue_game(choices):
  global score
  player_choice = get_player_choice(choices)
  while player_choice == "help":
    print_instructions()
    player_choice = get_player_choice(choices)

  if choice_is_correct(choices, player_choice):
    increase_score()
    choices = advance_to_next_question(choices)
    continue_game(choices)
  else:
    print("\nSorry, that was incorrect.")
    print(f"You reached a score of {score}\n")
    again = input("Game over.  Play again? y or n ")
    if again == "y":
      score = 0
      start_game()
    else:
      print("Goodbye!")


start_game()
