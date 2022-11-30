import random
import word_picker

def game_option_func():
    game_option = input('Which Wordle game would you like to play? Enter 1 to solve the New York Times Wordle or enter 2 to solve a randomly generated Wordle:')
    if game_option == '1':
        print('You selected the New York Times Wordle')
    elif game_option == '2':
        print('You selected a randomly generated Wordle')
    else:
        print('You did not enter a valid input')
        game_option_func()

    return game_option




#game_option_func()
