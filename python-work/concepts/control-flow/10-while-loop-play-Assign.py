# This code demonstrates a while loop with a "counting variable"
i = 0 # int
while i < 99: # jb tk i ki value 99 se chhoti nahi hojati/rehti
    print (i);
    i = i+1 # order --> pichli i ki value me k i plus hoga

# This uses a while loop to remove all the spaces from a string of
# text. Can you figure out how it works?

def remove_spaces(text): 
    text_without_spaces = '' #empty string for now
    while text != '': # space jo hai wo vvalue ke qual nahi hoajti answer print krna hai 
        # space to kabhi bhi value ke equal ho hi nai skti.
         next_character = text[0]
         if next_character != ' ':    #that's a single space
             text_without_spaces = text_without_spaces + next_character
         text = text[1:]
    return text_without_spaces
print (remove_spaces("hello my name is Owais how are you?"));