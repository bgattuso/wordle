import random
import word_picker
import game_option
from colorama import Fore, Back, Style, init

def user_interface():
    gameoption = game_option.game_option_func()
    if gameoption == '1':
        print('here')
    elif gameoption == '2':
        correctword = word_picker.word_picker()

    list_of_words = open('words.txt', 'r')
    guess = input('What is your first guess for the 5 letter word?:')
    guess = guess.lower()
    num_of_words = 12947
    line_counter = 0


    for line in list_of_words:
        word = line[:-1]
        if word != guess:
            line_counter = line_counter + 1
        if line_counter == num_of_words:
            if guess == 'death':
                line_counter = line_counter
            else:
                print('Your input is not a valid 5 letter word')
                guess = input('What is your first guess for the 5 letter word?:')
                guess = guess.lower()

    init(autoreset=True)

    guess_counter = 1

    while guess != correctword:
        #print(correctword)
        guess_counter = guess_counter + 1
        for i in range(len(guess)):
            gray_counter = 0
            guess_letter = guess[i]
            for l in range(len(correctword)):
                correct_letter = correctword[l]
                if guess_letter == correct_letter:
                    if guess[i] == correctword[i]:
                        print(Back.GREEN + guess[i])
                        break
                    elif guess[i] != correctword[i] and guess[l] != correctword[l]:
                        print(Back.YELLOW + guess[i])
                        break
                    elif guess[i] != correctword[i] and guess[l] == correctword[l]:
                        print(Back.WHITE + guess[i])
                        break
                else:
                    gray_counter = gray_counter + 1
                    if gray_counter == 5:
                        print(Back.WHITE + guess[i])
        list_of_words = open('words.txt', 'r')
        guess = input('What is your guess for the 5 letter word?:')
        guess = guess.lower()
        num_of_words = 12947
        line_counter = 0

        for line in list_of_words:
            word = line[:-1]
            if word != guess:
                line_counter = line_counter + 1
            if line_counter == num_of_words:
                if guess == 'death':
                    line_counter = line_counter
                else:
                    print('Your input is not a valid 5 letter word')
                    guess = input('What is your guess for the 5 letter word?:')
                    guess = guess.lower()


    if guess == correctword:
        print(Back.GREEN + guess[0])
        print(Back.GREEN + guess[1])
        print(Back.GREEN + guess[2])
        print(Back.GREEN + guess[3])
        print(Back.GREEN + guess[4])


    print('The word is', correctword)
    print('It took you', guess_counter, 'guesses to solve this Wordle')

    play_again = input('Do you want to play again? Enter y if yes, if not enter anything other than y to stop:')
    if play_again == 'y':
        user_interface()
    else:
        print('Thanks for playing!')


user_interface()
