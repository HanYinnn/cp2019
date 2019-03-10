#Write a program that prompts the user to enter the month and year, and displays the number of days in the month. 
#For example, if the user entered month 2 and year 2000, the program should display that February 2000 has 29 days. 
#If the user entered month 3 and year 2005, the program should display that March 2005 has 31 days.  

month = int(input('Enter Month: '))
year = int(input('Enter Year: '))
months = ["January", "February","March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
n = months[month-1]
t_d = [4,6,9,11]
t_o_d =[1,3,5,7,8,10,12]

if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and month == 2:
    print(n,"in",year,"has 29 days.")
elif month == 2:
    print(n,"in",year,"has 28 days.")
elif month in t_d:
    print( n,"in", year,"has 30 days.")
elif month in t_o_d:
    print(n,"in",year,"has 31 days.")    
