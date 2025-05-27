# if else pay programme - Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75) 

hours = input("Enter hours: ")
rate = input("Enter rate: ")

hours = float(hours)
rate = float(rate)

if hours <= 40:
    # print("Regiular")
    pay = hours * rate
    print(pay)
else:
    # print("Overtime")
    pay = 40 * rate + (hours - 40) * 1.5 * rate
    print("The pay is: ", pay)






# using try and except :

hours = input("Enter hours: ")
rate = input("Enter rate: ")

try :
    hours = float(hours)
    rate = float(rate)
    if hours <= 40:
    # print("Regiular")
        pay = hours * rate
        print(pay)
    else:
    # print("Overtime")
        pay = 40 * rate + (hours - 40) * 1.5 * rate
        print("The pay is: ", pay)

except :
    print("Enter a numerical value")






# method 2
    
hours = input("Enter hours: ")
rate = input("Enter rate: ")

try :
    hours = float(hours)
    rate = float(rate)

except :
    print("Enter a numerical value")
    quit()

if hours <= 40:
    pay = hours * rate
    print(pay)
else:
    pay = 40 * rate + (hours - 40) * 1.5 * rate
    print("The pay is: ", pay)









# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. 
#If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

grade = input("Enter the grade: ")
grade = float(grade)

if grade >= 0 and grade <= 1.0:
    if grade >= 0.9:
        print("A")
    elif grade >= 0.8:
        print("B")
    elif grade >= 0.7:
        print("C")
    elif grade >= 0.6:
        print("D")
    else:
        print("F")

else : 
    print("enter a correct value")


# using function, write pay program

def computepay():
    h = float(h)
    r = float(r)

    if h > 40:

        pay = 40*r + (h-40)*r*1.5

        return pay
    else :
        pay = h*r
        return pay
    
p = computepay()
print("Pay", p)

