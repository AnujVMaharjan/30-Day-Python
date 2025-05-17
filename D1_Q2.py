# Find an Euclidian distance between (2, 3) and (10, 8)
# Same as Pythagoras theorem, Hypotenuse

import math 

# Since tuples are immutable, lets try list

a= [2,3]
b= [10,8]

#underoot of (x2-x1)^2 + (y2-y1)^2

distance = math.sqrt(((b[0]-a[0])**2) + ((b[1]-a[1])**2))   # cannot use ^2 
                
print ("Euclidian distance = ", distance)
