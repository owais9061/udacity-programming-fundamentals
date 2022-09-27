# Define a procedure, is_friend, that
# takes a string as its input, and
# returns a Boolean indicating if
# the input string is the name of
# a friend. Assume I am friends with
# everyone whose name starts with D such as Daniya, Daud
# and no one else. You do not need to
# check for the lower case 'd'

def is_friend(name):
    if name[0]=="A":
        return True
    else:
        return False
    
print (is_friend('Abdul Rehman'));