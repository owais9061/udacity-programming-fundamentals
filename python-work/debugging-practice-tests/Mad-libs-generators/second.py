# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call 
# the procedure using the line
# countdown(3)
# instead of print countdown(3).

def countdown(number):
    i = number
    while (i>0):
        print(i)
        i -= 1 #breaking point of i
    print('Blastoff!')
countdown(2) #number 4 levels
#>>> 3
#>>> 2
#>>> 1
#>>> Blastoff!

