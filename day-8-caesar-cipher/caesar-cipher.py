alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar():
  cipher_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  start_text = input("Type your message:\n").lower()
  shift_amount = int(input("Type the shift number:\n"))
  end_text = ""
  shift_amount = shift_amount % len(alphabet)

  if cipher_direction == "decode":
    shift_amount *= -1

  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")
  
  play_again = input("Type 'yes' if you want to go again.  Otherwise type 'no'")
  if play_again == "yes":
    caesar()
  else:
    print("Goodbye.")

from art import logo
print(logo)

caesar()
