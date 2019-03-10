#Write a program that prompts the user to enter a score between 0 and 100 inclusive. The grading system is as follows: 
#A: 70 - 100
#B: 60 - 69
#C: 55 - 59
#D: 50 - 54
#E: 45 - 49
#S: 35 - 44
#U: 0 - 34

score = float(input("Enter a score: "))

if score in range(0,35):
    print("Grade: ", "U")
elif score in range(35,45):
    print("Grade:" , "S")
elif score in range(45,50):
    print("Grade:" , "E")
elif score in range(50,55):
    print("Grade:" , "D")
elif score in range(55,60):
    print("Grade:" , "C")
elif score in range(60,70):
    print("Grade:" , "B")
elif score in range(70,101):
     print("Grade:" , "A")
else:
    print("Invalid score!!", "Enter score in range 1 to 100")
