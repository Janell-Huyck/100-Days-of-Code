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
choices_images = [rock, paper, scissors]
choices_words = ["rock", "paper", "scissors"]
choices_numbers = [0,1,2]

print("Welcome to Rock, Paper, Scissors\n")

user_choice = int(input("What do you choose?  Type 0 for Rock, 1 for Paper, or 2 for Scissors."))
print(f"You chose {choices_words[user_choice]}.")
print(choices_images[user_choice])

computer_choice = random.randint(0,2)
print(f"The computer chose {choices_words[computer_choice]}.")
print(choices_images[computer_choice])

#If result is a draw
if user_choice == computer_choice:
  print("The game is a draw.")

#If the player wins
elif choices_numbers[user_choice - 1] == computer_choice:
  print("You won!")

#The computer won
else: 
  print("Sorry, you didn't win this time.")
  
