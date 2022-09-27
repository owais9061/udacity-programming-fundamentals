# Let's put it all together. Write code for the function process_madlib, which takes in 
# a string "madlib" and returns the string "processed", where each instance of
# "NOUN" is replaced with a random noun and each instance of "VERB" is 
# replaced with a random verb. You're free to change what the random functions
# return as verbs or nouns for your own fun, but for submissions keep the code the way it is!

from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "RUN"
    else:
        return "WALK"
        
def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "BSOC"
    else:
        return "Academy"

def word_transformer(word):
    if word == "NOUN": # meri string me jaha bhi lafz NOUN mention hoga wo usko replace krdega random noun se or phir uski limit dekhega (0,1)
        return random_noun()
    elif word == "VERB":
        return random_verb()
    else:
        return word[0] #string indexation (agr hamain string ke aik particular part ko print krwana ho )
        
def process_madlib(mad_lib):
    processed = ""
    
    # your code here
    # yahan per ( len ) function use hoga....!!
    
test_string_1 = "This is a good NOUN to use when you VERB your food"
test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
print (process_madlib(test_string_1))
print (process_madlib(test_string_2))