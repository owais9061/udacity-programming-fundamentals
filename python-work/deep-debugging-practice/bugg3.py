# Try adding print statements to look at the values of variables inside
# the remove function.  See if you can find out what's making it give
# silly answers such as remove('ding', 'do') -> 'dining'.

def remove(somestring, sub):
    """Return somestring with sub removed."""
    #this line of code means to find the sub(which is the chracter to be removed) in the location
    location = somestring.find(sub) 
    if location == -1:
        return somestring
    
    #Select out the number of elements of SUB
    length = len(sub) 
    
    #Somestring's first part that is the part after the first word 0 --> location
    part_before = somestring[:location] 
    
    # to print after the location part 
    part_after = somestring[location + length:]  
    return part_before + part_after  #Here finally the function (remove) we created above wilreturn output of part before + part aftr

# 
# Don't change these test cases!
print (remove('Bsoc Academy', 'Bsoc'))
print (remove('pythonic', 'ic'))
print (remove('substring institution', 'string in'))
print (remove('ding', 'do'))  # "do" isn't in "ding"; should print "ding"
print (remove('doomy', 'dooming'))  # and this should print "doomy"


#here we get propr outputs but lets just change the functiona little and then replace + with ,


def remove(somestring, sub):
    """Return somestring with sub removed."""
    #this line of code means to find the sub(which is the chracter to be removed) in the location
    location = somestring.find(sub) 
    
    #Select out the number of elements of SUB
    length = len(sub) 
    
    #Somestring's first part that is the part after the first word 0 --> location
    part_before = somestring[:location] 
    
    # to print after the location part 
    part_after = somestring[location + length:]  
    return part_before + part_after  #Here finally the function (remove) we created above wilreturn output of part before + part aftr

# 
# Don't change these test cases!
print (remove('Bsoc Academy', 'Bsoc'))
print (remove('pythonic', 'ic'))
print (remove('substring institution', 'string in'))
print (remove('ding', 'do'))  # "do" isn't in "ding"; should print "ding"
print (remove('doomy', 'dooming'))  # and this should print "doomy"

#now the above cod will give erros because the , make the parts (location and sub to be appear has parts of strings)  # not indices
#read above statement again PROPERLY !!!!!!!

#  smrahze    zehra
samrah





