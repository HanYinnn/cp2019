#Write a program q1_fahrenheit_to_celsius.py that reads a Fahrenheit degree in double (floating point / decimal) from standard input, 
#then converts it to Celsius and displays the result in standard output. 
#The formula for the conversion is as follows: celsius = (5/9) * (fahrenheit - 32)

#get input
Fahrenheit = int(input ("Enter temperature in Fahrenheit:")) # use integer function to convert it into numbers

#compute celsius temperature
celsius = (5/9) * (Fahrenheit - 32)

#output result
print("{0:.1f}".format(celsius)) # 0 means the first thing to print 
