#Write a program that displays the following two tables side-by-side (note that 1 mile is 1.609 kilometres):

#Miles	Kilometers	Kilometres	Miles
#1    	1.609     	20        	12.430
#2    	3.218     	25        	15.538

#...
#9    	14.481    	60        	37.290
#10   	16.090    	65        	40.398

print("Miles""\t""Kilometers""\t\t""Kilometers""\t""Miles")
for i in range(1,11):
    print(i, " "*(6-(len(str(i)))), (i*1.609)," "*(22-len(str(i*1.609))),(i*5+20), " "*(14-len(str(i*5+20))),"{0:.3f}".format((i*5+20)/1.609 ))
