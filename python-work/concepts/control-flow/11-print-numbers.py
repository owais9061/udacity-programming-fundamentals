# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints 
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.
def numbers(n):
    n = 1 # starting point , for loop we used another variable i
    while  ( n < 10 ):  # <= is less than an equal to
        n += 2 # order
print(numbers(6))  # this thing is called a block of while loop
        
# print(numbers(6)); # number in braces determine the limit

# Above numbers in the braces can be replace by recalling a function of python which is breakpoint, but we will not use it here becuase it is a little more complex.