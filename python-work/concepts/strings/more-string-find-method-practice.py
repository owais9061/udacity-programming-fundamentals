# This segment is just a chance for you to play around with 
# finding strings within strings. Read through the code and 
# press Test Run to see what it does. Is there anything 
# interesting or unexpected?

print ("Example 1: using find to print the second occurrence of a sub-string")
print ('test'.find("t"));
print ('test'.find("t", 1));
#here are two "t's" so it print the last one after 1.

print ("Example 2: using a variable to store first location");
first_location = ('test'.find("t")); # here we store the first location of "t"
print ('test'.find("t", first_location+1)); # then we use that location to find the second occurrence.

print ("Example 3: using find to get rid of exclamation marks!!");
example = "Wow! Python is great! Don't you think?";
first = example.find('!'); #answer should be 3 & 20
second = example.find('!', first + 1) #answer should be 24
new_string = example[:first] + example[first+1:second] + example[second+1:] 
#above line of code has 3 part
#part 1 is from first quotation to last w of Wow
#part 2 is from the space after first ! sign , to the ! sign after t of great
#part 3 is from the space after ! of great to the last Quotation mark.

print (new_string); # oops, I should probably replace the !s with periods
new_string = example[:first] +'.'+ example[first+1:second] +'.'+ example[second+1:]
print (new_string);

#THis is a little complex for a beginner but truely a useful method for someone who is
#willing to pursue Data Science.