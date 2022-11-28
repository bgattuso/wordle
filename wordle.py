import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver')
url = 'https://www.nytimes.com/games/wordle/index.html'
driver.get(url)
body = driver.find_element(By.XPATH, f'//body')
body.click()


guesses = ['stead', 'flung', 'womby', 'chirp']
for guess in guesses:
    body.send_keys(guess + Keys.ENTER)
    time.sleep(3)

game_app = driver.find_elements(By.CSS_SELECTOR, 'game-app')[0].shadow_root
game_theme_manager = game_app.find_elements(By.CSS_SELECTOR, 'game-theme-manager')[0]
keyboard = game_theme_manager.find_elements(By.CSS_SELECTOR, 'game-keyboard')[0].shadow_root
buttons = {}

for button in keyboard.find_elements(By.CSS_SELECTOR, 'button'):
    dataset = button.get_property('dataset')
    buttons[dataset.get('key')] = dataset.get('state', 'notguessed')

result_array = [[buttons[letter] for letter in word] for word in guesses]

time.sleep(5)
print(result_array)

target = [None] * 5
wrong_space = {}
for i, result in enumerate(result_array):
    for j, state in enumerate(result):
        if state == ['absent', 'notguessed']:
            continue
        letter = guesses[i][j]
        if state == 'correct':
            target[j] = letter
        elif state == 'present':
            spaces = wrong_space.get(letter, [])
            spaces.append(j)
            wrong_space[letter] = spaces
print(target)

letters_left = ["q","v","x","z","j","k"]
for space in wrong_space:
    print(space)
    letters_left.append(space)

for space in target:
    if space is not None:
        letters_left.append(space)

print(letters_left)

with open('words.txt') as f:
    word_list = list(f)
counter = 0
new_list = []
for word in word_list:
    counter = 0
    for letter in letters_left:
        if letter in word:
            counter += 1
    if counter == 5:
        new_list.append(word)
        print(word + "\n")

slay = []
for i in range(len(new_list)):
    slay.append(0)

for i in range(len(new_list)):
    for x in range(len(target)):
        if new_list[i][x] == target[x]:
            slay[i] = slay[i] + 2
    for space in wrong_space:
        if space in new_list[i][x]:
            slay[i] = slay[i] + 1

highest_num = 0
index = 0
for i in range(len(new_list)):
    if slay[i] > highest_num:
        highest_num = slay[i]
        index = i

next_guess = new_list[index]
body.send_keys(next_guess + Keys.ENTER)

