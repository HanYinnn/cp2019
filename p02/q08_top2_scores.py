list = {}
i = int(input("Enter total number of students: "))

for i in range (0,i):
    name = input("Enter student's name: ")
    score = input("Enter student's score: ")
    list[score] = name
    
print(list)
print(list[max(list.keys())] + " got the highest score, " + max(list.keys()) + "." )
del list[max(list.keys())]
print(list[max(list.keys())] + " got the second highest score, " + max(list.keys()) + ".")
