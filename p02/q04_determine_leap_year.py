#Write a program that prompts the user to enter a year and determines whether it is a leap year. 
#A year is a leap year if it is divisible by 4 but not 100, or is divisible by 400. 

#input
year = int(input("Enter a year to determine if it is a leap year: "))

#compute
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Its a leap year!")
else:
    print("Its not a leap year :( ")
