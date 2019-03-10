#Write a program that displays the following table (1 kilogram = 2.2 pounds):

#Kilograms Pounds
#1         2.2
#2         4.4
#3         6.6
#...
#9         19.8
#10        22.0



value = [[1, 2.2], [2,4.4],[3 , 6.6],[4 , 8.8],[5 ,11.0], [6 , 13.2],[7 , 15.4],[8, 17.0],[9, 19.8]]  #list in a list

print("kilogram  pounds ")

for items in value:
       print(items[0], " "*(12-len(str(items[1]))), items[1])
