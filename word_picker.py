import random

def word_picker():
    list_of_words = open('words.txt', 'r')
    num_of_words = 12947
    line_counter = 0
    random_number = random.randint(1, num_of_words)
    #print(random_number)

    for line in list_of_words:
        correct_word = line[:-1]
        line_counter = line_counter + 1
        if line_counter == random_number:
            break

    if random_number == num_of_words:
        correct_word = 'death'

    return correct_word
    #print(correct_word)


word_picker()
