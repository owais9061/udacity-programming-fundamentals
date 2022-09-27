# Given the variables defined here, write Python 
# code that prints out the distance, in meters, 
# that light travels in one processor cycle. 

# speed_of_light in meters per second
# cycles_per_second is 2.7 GHz


speed_of_light = 299792458.0 ;
cycles_per_second = 2700000000.0;
distance= speed_of_light/cycles_per_second;
print(distance);


#Just remember variables can variate & Python follow
#semantice order which means the most lastest created variable
#will be utilized 
#such as above we created a variable of cycles_per_second = 2700000000
#Now i change it to 
cycles_per_second = 1800000000;
distance= speed_of_light/cycles_per_second;
#Now if i print the distance it will give me a different value

print(distance);