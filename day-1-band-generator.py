# Repl: https://replit.com/@JanellHuyck/band-name-generator-start#main.py
# Takes input from the user and turns it into a proposed name for a band.

#1. Create a greeting for your program.
print("Welcome to the Band Name Generator")
#2. Ask the user for the city that they grew up in.
city_name = input("What city did you grow up in?\n")
#3. Ask the user for the name of a pet.
pet_name = input("What is the name of a pet?\n")
#4. Combine the name of their city and pet and show them their band name.
band_name = city_name + " " + pet_name
print("Your band name could be: " + band_name)
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end
