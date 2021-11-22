import random
from hangman_words import word_list
from hangman_art import logo, stages
from replit import clear

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
guessed_letters = []

end_of_game = False
lives = 6

print(logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    print(f"You have guessed: {(', '.join(guessed_letters)) if len(guessed_letters) > 0 else 'nothing yet!'}")
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in guessed_letters:
      print(f"You have already guessed {guess}")

    guessed_letters.append(guess)

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"Your guess of {guess} is not in the word.  You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose.  The word was {chosen_word}.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
