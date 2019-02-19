# get input     # when running big programme read code
weight = int(input("Enter weight(kg): "))
height = float(input("Enter height(m):"))

#compute bmi 
bmi =weight / (height *height)

#output result
print("BMI ={0:.2f}".format(bmi))
if bmi < 18.5:
    print("please eat more")
elif 18.5 <= bmi <23:
    print("low risk")
elif 23 <= bmi <= 27.5:
    print("moderate risk")
else: # >=27.5
    print("high risk")
