from all_games.guess_game import guess_game as guess_game
from all_games.currency_roulette_game import currency_roulette as currency_roulette
from all_games.memory_game import memory_game as memory_game
import sys

class wog_setup(object):
    def ask_for_another_game():
        ask_user = str(input('Want to play another game?  y/n ')).lower()
        if ask_user.startswith('y'):
            wog_setup.another_game_level()

        elif ask_user.startswith('n'):
            print('Bye Bye')
            sys.exit()

        else:
            print('Please select y/n')
            wog_setup.ask_for_another_game()


    def another_game_level():
        ask_user_level = input("Select difficulty level >")

        if ask_user_level.isdigit():
            if 1 <= int(ask_user_level) <= 5:
                print(f"Selected level: {ask_user_level}")
                global chosen_game
                globals()[chosen_game](int(ask_user_level))
            else:
                print(f'{ask_user_level} is not it the range between 1 and 5')
                wog_setup.another_game_level()
        else:
            print("Enter a number, not a stirng")
            wog_setup.another_game_level()

    def welcome():
        print(f"Hi {str(input('Enter you name here  --> '))} and welcome to the World of Games: The Epic Journeyn\n\n"
              f"*** Note that you can exit at any moment by type: 'exit' ***\n")

    def start_play():
        global list_of_games
        list_of_games = [
            "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back",
            "2. Guess Game - guess a number and see if you chose like the computer",
            "3. Currency Roulette - try and guess the value of a random amount of USD in ILS"]
        print("Games available to play:"),[print(game) for game in list_of_games]

        while True:
            user_game_choice = input("Please choose a game to play (enter game number) --> ")
            if user_game_choice.lower() == 'exit': sys.exit()
            if user_game_choice.isdigit() and 1 <= int(user_game_choice) <= len(list_of_games): break
            print(f"{f'Enter a valid game number between 1-{len(list_of_games)}' if user_game_choice.isdigit() else 'Enter a number, not a stirng'}")

        while True:
            user_game_level = input(f"\n---- {str(list_of_games[int(user_game_choice) - 1]).split('.')[1]} ----\n"
                                    "Select difficulty level between 1 and 5 (1-easiest 5 most difficult) --> ")
            if user_game_level.lower() == 'exit': sys.exit()
            if user_game_level.isdigit() and 1 <= (level := int(user_game_level)) <= 5: print(f"Selected level: {level}"); break
            print(f"{f'{user_game_level} is not it the range between 1 and 5' if user_game_level.isdigit() else 'Enter a number, not a stirng'}")
        global chosen_game
        chosen_game = str(list_of_games[int(user_game_choice)-1].split(".")[1].split("-")[0]).strip().replace(" ","_").lower()
        globals()[chosen_game](int(user_game_level))

        while True:
            wog_setup.ask_for_another_game()