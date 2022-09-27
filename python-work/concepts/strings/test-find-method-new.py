#till here we have worked with find method to locate a single string
#but now we will use two strings find method
#for example
#let's say
print('BSOC is a leading coding academy'.find("B"));
#on printing this is will show the index ), because B is at 0
#now
print('BSOC is a leading coding academy'.find("O"));
#this will tell the position of ) with is 2
#Now
#if we give a command like this
print('BSOC is a leading coding academy'.find("leading",10));

#Read this carefull
#TIll now the position of Leeading is at 10, and i have given
#give another string like 11 or 12, it will print out (-1) which is error so
#we will add another leading in the string like this

print('BSOC is a leading coding & leading academy'.find("leading",12));
#now if i type in 11 with the leading it will correspond to the next leading in the string, leavng behind the first one
#which means our error will be resolved.