#this program will create a proram which will make
#computer guess the number we have think

#same code s prevous one but with some adition
import random 

def guess(x): # X is set as parametre for random digit
    random_number = random.randint(1, x) # random number between 1 to x 
    # use of while loops
    guess = 0
    while guess != random_number: # stop the expression when guessed number is equal to generated number
        guess = int(input(f'Guess a Number between 1 & {x}: '))
        # USE OF if STATEMENT
        if guess < random_number:
            print('Sorry, guess again. Too Low')
        elif guess > random_number:
            print('Sorry, guess again. Too High')
    
    print(f'Yay, Congrats! You have guesses the number correctly {random_number} ')
        
guess(15) # number of trials

def computer_guess(x):
    low = 1
    high= x
    # intiate feedback variable
    feeback = ''
    #when it's correct
    while feedback != 'c':
        guess = random.randint(low, high) # we set high and low to set boundries in between we will guess the numbers to be
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C) ?? ').lower()
    