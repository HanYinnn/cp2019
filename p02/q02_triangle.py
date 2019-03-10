#Write a program that reads three edges for a triangle and determines whether the input is valid.
#The input is valid if the sum of any two edges is greater than the third edge. 
#The program will compute the perimeter of the triangle if the input is valid. Otherwise, display that the input is invalid. 

S1 = float(input("Enter an side 1: "))
S2 = float(input("Enter an side 2: "))
S3 = float(input("Enter an side 3: "))

if S1 + S2 > S3 or S2 + S3 > S1 or S1 + S3 > S2:
    print("Valid Triangle!")
else:
    print("Invalid Triangle!")
