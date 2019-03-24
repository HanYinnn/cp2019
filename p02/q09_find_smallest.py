#Use a while loop to find the smallest integer n such that n2 is greater than 12,000. 

import math
n = math.sqrt(12000)

while True:
    if n ** n > 12000:
        print("The smallest integer is: ", n)
        break
    
    
