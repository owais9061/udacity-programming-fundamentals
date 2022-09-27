# output input functions
# while loops
# if else elif
# operators greater than less tha etc.

import random

def guess(x):
    random_number= random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a new Number between 1 & {x} '))
        if guess < random_number:
            print('Sorry , guess again. Too Low')
        elif guess > random_number:
            print('Sorry, guess again. Too High')
            
    print(f'Yay, Congrats! You have guess the right Number {random_number}')

guess(15);



