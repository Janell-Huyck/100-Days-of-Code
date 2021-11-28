#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import os
from art import logo
import random

def print_logo():
  os.system('cls||clear')
  print(logo)
  print("""
    Welcome to High - Low, a number guessing game.
    The computer has selected a random integer between
    one and a hundred (inclusive).  Your task is to 
    guess what that number is.  After every guess, you 
    will be given a hint to help you refine your guess.
    Good luck!\n
  """)

def generate_random_number():
  random_number = random.randint(1,100)
  print(f"Psssst.  The number is {random_number}.")
  return random_number

def set_initial_difficulty():
  difficulty = input("What difficulty level would you like?  Type 'easy' or 'hard'. ").lower()
  if difficulty == "easy":
    print("You start with 10 guesses.")
    initial_guesses = 10
  elif difficulty == "hard":
    print("You start with 5 guesses.")
    initial_guesses = 5
  else:
    print("Oh, so you really want a challenge?  >:) You get 3 guesses.")
    initial_guesses = 3
  return initial_guesses

def get_player_guess():
  player_guess = "nothing"
  while not player_guess.isnumeric():
    player_guess = input("Please make a guess from 1 to 100: ")
  return int(player_guess)

def display_guesses_left(guesses_left):
  print(f"You have {guesses_left} guesses remaining.")

def compare_guess(guess, actual):
  if guess < actual:
    print("Too low.")
    return False
  elif guess > actual:
    print("Too high.")
    return False
  else:
    print(f"You got it!  The number was {actual}.")
    return True

def play_again():
  again = input("Play again?  y or n: ").lower()
  if again == "y":
    play_game()
  else:
    print("Thank you for playing. Goodbye!")
    return

def play_game():
  print_logo()
  actual_number = generate_random_number()
  guesses_left = set_initial_difficulty()
  while guesses_left > 0:
    display_guesses_left(guesses_left)
    player_guess = get_player_guess()
    if compare_guess(player_guess, actual_number) == True:
      play_again()
      return
    else:
      guesses_left -= 1
  print(f"Sorry.  You lose.  The acutal number was {actual_number}.")
  play_again()


play_game()
