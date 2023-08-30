from random import randint
import sys
def guess_game(difficulty_level):
    randon_number = randint(0,int(difficulty_level))
    guesses_number = 0
    while True:
        user_guess = input("Your guess is: ")
        if user_guess.lower() == 'exit': sys.exit()

        elif user_guess.isdigit():
            user_guess = int(user_guess)
            print("your guess is too high" if user_guess > randon_number else("your guess is too small" if user_guess < randon_number else "")); guesses_number += 1

            if user_guess == randon_number:
                print(f"Well done!\nIt took you {guesses_number} guesses") ;break

        else:
            print("Please enter a number and not a stirng")