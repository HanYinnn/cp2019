#Write a program q3_miles_to_kilometre.py that reads a number in miles, converts it to kilometres, and displays the result. 
#One mile is 1.60934 kilometres. Display your answer correct to 3 decimal places

#get input
miles = int(input("Enter miles: "))    

#compute miles to kilometer
kilometer = miles * 1.60934

#get output
print("{0:.3f}".format(kilometer))
