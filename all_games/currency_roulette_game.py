import sys
import yfinance as yf
from random import randint
from score import add_score

def currency_roulette(difficulty_level):
    randon_number = randint(1, 300)
    print(f"Guess how much {randon_number}$ are in shekels")
    cuurency_rate = round(yf.Ticker("ILS=X").history(period="1d")["Close"].iloc[0],3)
    amount_in_ils = int(float(cuurency_rate)*int(randon_number))
    guesses_number = 0
    while True:
        user_guess = input("Your guess is: ")
        if user_guess.lower() == 'exit': sys.exit()

        elif user_guess.isdigit():
            user_guess = int(user_guess)

            if abs(user_guess - amount_in_ils) <= int(6-difficulty_level):
                print(f"Well done!\nIt took you {guesses_number} guesses\nCurrency rate USD/ILS is: {cuurency_rate}")
                add_score(difficulty_level)
                break

            print("your guess is too high" if user_guess > amount_in_ils else ("your guess is too small" if user_guess < amount_in_ils else "")); guesses_number += 1

        else:
            print("Please enter a number and not a stirng")