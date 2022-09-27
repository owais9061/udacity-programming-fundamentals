#THis particular method is used to locate or find
# a string in a list of strings
#for example
sample="Hy, I'm Owais Chaudhry, a Computer Science Undergrad. at Iqra University"
#Now from the above string if i have to print out the index of my name
#i will do
print(sample.find('Owais Chaudhry'));
# it will give outout of 8, which means O of owais is at 8 number and now if i print
print (sample[8:]);
#this will print out the entire string from owais Chaudhry & owwards


#and if something is not in the given string that you have commanded to print
#then it will show a (-1) error like this
print (sample.find('Software'));

#Simple.......