# Write code for the function random_noun, which takes in no inputs but outputs 
# one of two nouns randomly. Use the randint function to generate a number 
# from 0-1 and return a noun depending on whether the number is equal to 0 or 1. 
# Feel free to experiment with different nouns, but for submission purposes return 
# the string "sofa" if the number is 0, else return "llama".

# to generate random Nouns

from random import randint

def random_noun():  # parameter assign nahi kia (ku nai kia) kuki isme mujhe direct output nahi chahie 
    random_num = randint(0,1)
    if random_num == 0: # age to wo number 0 hoga to prnt hoa "BSOC"
        return "BSOC"
    else:
        return "Academy"
    
def random_verb():  # parameter assign nahi kia (ku nai kia) kuki isme mujhe direct output nahi chahie 
    random_num = randint(0,1)
    if random_num == 0: # age to wo number 0 hoga to prnt hoa "BSOC"
        return "RUN"
    else:
        return "WALK"
    
# iska use case hai apka project jo MadLibs Final Project 
    
    
    