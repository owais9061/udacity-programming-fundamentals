# solve by seraching on the google the entire problem and then pasting the sample code in
# then slowly  make little changes till you came close to the code you write

# When I wrote boldwrap, I didn't copy the functionality of the
# bracket function carefully.  Review my code and catch the mistake.

# The Errors found in this problem are Syntax & Index

def bracket(text):
   return '[' + text + ']'

def boldwrap(text):
   return '<b>' + text + '</b>'

print (boldwrap('This is an important message.'))