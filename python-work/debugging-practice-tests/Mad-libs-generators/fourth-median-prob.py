# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

#def bigger(a,b):
    #if a > b:
        #return a
    #else:
        #return b

#def biggest(a,b,c):
    #return bigger(a,bigger(b,c))

#Anything done in median function is self based
#def median(a,b,c):
    #if bigger(a,b) <= c:
        #return(bigger(a,b))
    #if bigger(a,c) <= b:
        #return(bigger(a,c)) 
    #if bigger(b,c) <= a:
        #return(b,c)

#print(median(1,2,3))
#>>> 2

#print(median(9,3,6))
#>>> 6

#print(median(7,8,7))
#>>> 7



number1 = int(input("Please first number:"))
number2 = int(input("Please second number:"))
number3 = int(input("Please third number:"))
result = (number1 + number2 + number3) / 3

print("The average of three numbers: " , result)