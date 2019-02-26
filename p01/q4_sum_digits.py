#Write a program q4_sum_digits.py that reads an integer between 0 and 1000 and adds all the digits in the integer. 
#For example, if an integer is 932, the sum of all its digits is 14.
#Hint: Use the % operator to extract digits, and use the // operator to remove the extracted digit. 
#For instance, 932 % 10 = 2 and 932 // 10 = 93 

#input
number = int(input("Enter an integer: "))

#compute data
x = number % 10
y = number // 10
digit = x + y

#get output
print ("{0}".format(digit))
