from random import choice
from collections import Counter

fruits_name = """apple banana mango strawberry  
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon""".strip().split()

random_fruit_name = choice(fruits_name)
letter_guessed = ''
chances = len(random_fruit_name) + 2
flag = 0
correct_guess = 0

print('Guess the word! HINT: word is a name of fruit')
for _ in random_fruit_name:
    print('_', end = ' ')
print('\n')

while (chances != 0 and flag == 0):
    guess_letter = input('Enter a letter to guess:- ')
    chances -= 1
    if (not guess_letter.isalpha()) or (len(guess_letter) > 1):
        print('Enter only single letter')
        continue
    elif guess_letter in letter_guessed:
        print('You have already guessed the number')
        continue
    
    # if letter guess is corret
    if guess_letter in random_fruit_name:
        # if word has more than one same letter
        occurs = random_fruit_name.count(guess_letter)

        for _ in range(occurs):
            letter_guessed += guess_letter
    
    # print the char
    for char in random_fruit_name:
        if char in letter_guessed and (Counter(letter_guessed) != Counter(random_fruit_name)):
            print(char, end=' ')
            correct_guess += 1
        elif (Counter(letter_guessed) == Counter(random_fruit_name)):
            print(f'The word was {random_fruit_name}')
            print('Congratulations!, you won the game!!')
            flag = 1
            break
        else:
            print('_', end = ' ')
    print('\n')  

if chances <= 0 and Counter(letter_guessed) != Counter(random_fruit_name):
    print('=================')
    print(f'The word was {random_fruit_name}')
    print('You lost! Try again...')
