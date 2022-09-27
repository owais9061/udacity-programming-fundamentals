#Practice with Owais
#Next, Owais will ask you to write a function that adds the letter U to the beginning of strings. This is just meant to give you another chance at defining a function with the proper syntax.
# Some things to keep in mind:

# On the first line of your function definition…
# You must begin the line with def (lowercase).
# After def you must give a function name (in this case it will be bsocify).
# Next, you must have a set of parentheses with the required parameters inside.
# The line must end with a : colon.
# In the body of the function
# Every line in the function must be indented.
# If you want your function to produce output, it must end with a return statement.
# To "call" the function…
# "Calling" a function just means using it.
# You do this by writing:

# The function name, followed by
# an open paren (, followed by
# the values for the required parameters, followed by
# a closed paren ).
# To display the results of a function call.
# Don't forget to include the print command before you call your function if you want to display the result on your screen!

#Now the actual task!!!

# Define a procedure, bsocify, that takes as
# input a string, and returns a string that
# is an uppercase 'B' followed by the input string.
# for example, when you enter

# print bsocify('bsocians')

# the output should be the string 'Bsocians'
# Remove the hash, #, from infront of print to test your code.

def bsocify(a):
    return 'B' + a
print (bsocify('socians'))
#>>> Bsocians