# Set noun_replacement and verb_replacement to your own noun and verb strings. 
# Then, concatenate the variables substring1-3, noun_replacement, and 
# verb_replacement and assign the result to the variable new_sentence so that 
# it's in the same order as the variable sentence.

sentence = "A NOUN went on a walk. It can VERB really fast."
substring1 = sentence[0:2]
substring2 = sentence[6:30]
substring3 = sentence[34:]

noun_replacement = "Owais" # your noun here
verb_replacement = "Run" # your verb here

new_sentence = substring1 + noun_replacement + substring2 + verb_replacement + substring3;
print(new_sentence);

#also a method
sentence = "A NOUN went on a walk. It can VERB really fast."
print(sentence.replace('NOUN', 'OWAIS'));
print(sentence.replace('VERB','RUN'))
#substring1 = sentence[0:2]
#substring2 = sentence[6:30]
#substring3 = sentence[34:]

#noun_replacement = "Owais" # your noun here
#verb_replacement = "Run" # your verb here

#stacking method
#new_sentence = substring1;
#new_sentence = new_sentence + noun_replacement; # A + Owais
#new_sentence = new_sentence + substring2; # A Owais + Went on a walk, it can 
#new_sentence = new_sentence + verb_replacement; # A Owais + Went on a walk, it can  + Run
#new_sentence = new_sentence + substring3;
#print(new_sentence);
