from math import log
from random import randint

lower_number = int(input('Enter lower bound:- '))
upper_number = int(input('Enter upper bound:- '))

random_number = randint(lower_number, upper_number)
guess_time = round(log(upper_number - lower_number + 1, 2))
count = 0

print(f"\tYou've only {guess_time} chances to guess the number")
while count < guess_time:
    guess_number = int(input('Guess a number:- '))

    if guess_number == random_number:
        print(f"Congratulations you did it in {count + 1} guesses")
        break
    elif guess_number > random_number:
        print('Try Again! You guessed too high!')
    elif guess_number < random_number:
        print('Try Again! You guessed too small!!')
    
    count += 1
    
# if guessing is required more than guess number
if count >= guess_time:
    print(f'\nThe number is {random_number}')
    print('Better luck next time!')