# Define a procedure, abbaize, that takes
# two strings as its inputs, and returns
# a string that is the first input,a
# followed by two repetitions of the second input, b * 2
# followed by the first input a

def abbaize(a,b):
    ans = a + b*2 + a
    return ans

print (abbaize('abdul','samrah'));

#also try out this...

def abbaize(a,b):
    ans = a + b*2 + a
    return ans
print (abbaize('dog','cat'))
