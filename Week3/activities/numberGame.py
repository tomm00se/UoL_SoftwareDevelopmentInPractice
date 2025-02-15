# Exercise: Guess a number between 1 and 9

import random

target_num, guess_num = random.randint(1, 10), 0

while target_num != guess_num:
    guess_num = int(input("Guess a number between 1 and 9 until you get it right: "))
    print("You guessed the number: ", guess_num)

print("Congratulations! You guessed the correct number!")