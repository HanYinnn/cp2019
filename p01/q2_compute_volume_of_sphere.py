#C reads in the radius and length of a cylinder and computes its volume using the following formulae:
#area = radius * radius * pi
#volume = area * length

from math import pi

#get input
radius = int(input("Enter radius: "))
length = int(input("Enter length: "))

#compute area and volume
area = radius * radius * pi
volume = area * length

#output result
print ("{0:.1f}".format(volume))
