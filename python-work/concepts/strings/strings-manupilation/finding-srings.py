# Use the string.find method to locate "NOUN" and "VERB" in the string text
# and store those positions in the variables noun_position and verb_position respectively.

text = """Wow this is a fairly long body of text. Quite a few characters too.
I wonder if the string.find method could help find where NOUN is located.
That way, I could go out and VERB with my friends rather than counting characters
all day long!"""

print(text.find('VERB'));
#above code was wrtiten to find out the positions of NOUN & VERB
noun_position = text[125:130];
verb_position = text[171:176];
print(noun_position , verb_position);