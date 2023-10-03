from random import randint
import time, re,sys
import os
from score import add_score
from utils import clean_screen
def memory_game(difficulty_level):
    randon_numbers = [randint(1, 101) for _ in range(difficulty_level)]
    print(f'Remember the numbers:\n{randon_numbers}'), time.sleep(2)
    clean_screen()

    user_guesses = input("Your numbers are: ")
    numbers_list = re.findall(r'\d+', user_guesses)
    user_numbers = [int(number) for number in numbers_list]
    count_guesses = 0
    while True:
        if user_guesses.lower() == 'exit': sys.exit()

        elif set(user_numbers) == set(randon_numbers):
            print(f"Well done!\nit took you {count_guesses} times")
            add_score(difficulty_level)
            break

        else:
            for user_guess in user_numbers:
                if int(user_guess) in randon_numbers:
                    continue
                else:
                    print(f'{int(user_guess)} was not in tht list, try again')
                    count_guesses += 1
                    user_guesses = input("Your new numbers are:\n")
                    numbers_list = re.findall(r'\d+', user_guesses)
                    user_numbers = [int(number) for number in numbers_list]