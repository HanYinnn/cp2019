#Write a program q7_generate_payroll.py that reads the following information and prints a payroll statement. 
#A sample input and output session is as follows:


#input
w = str(input("Enter name: ")) 
x = int(input("Enter the number of hours worked weekly: "))
y = float(input("Enter hourly pay rate: "))
z = float(input("Enter CPF contribution rate(%): "))

#compute gross pay
gross_pay = y * x
CPF_contribution = z /100 * gross_pay
net_pay = gross_pay - CPF_contribution


#output
print("Payroll statement for", "{0}".format(w))
print("Number of hours worked in week: ", "{0}".format(x))
print("Hourly pay rate: $","{0}".format(y))
print("Gross pay =  $","{0:.1f}".format(gross_pay))
print("CPF contribution at 20% = $","{0:.2f}".format(CPF_contribution))
print("Net pay = $","{0:.2f}".format(net_pay))

