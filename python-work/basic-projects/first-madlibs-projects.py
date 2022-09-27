# String concatenation concept is being used here
# suppose we want to create a string that says" join the ________"
# academy= " BSOC " some strings

# some ways to handle this problem can be
#print {"Join the  "  + Academy}
#print ("join the {}".format{academy})
#print(f"join the {academy})

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
academy_name = input("Academy Name: ") #as a prompt

madlib = f"Computer Coding is so {adj}! it makes us so excited but in excitment we forget that we love to {verb1}. so stay hydrated and {verb2} as we instruct at {academy_name}!"
    
print(madlib);

#Madlib basically mean mad library used basicallly for fun purpose.
#You can create so many of these for nouns, pronouns and verbs and adjectives