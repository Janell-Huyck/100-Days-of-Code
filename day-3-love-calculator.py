# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()
true_count = 0
love_count = 0

def count_letters(name, word):
    result = 0
    for letter in word:
        result += name.count(letter)
    return result

true_count = count_letters(name1, "true") + count_letters(name2, "true")
love_count = count_letters(name1, "love") + count_letters(name2, "love")

score = int(str(true_count) + str(love_count))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")

