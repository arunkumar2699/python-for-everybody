# Exercise 1.1 : Write Hello World! in python
print("Hello World!")


# Exercise 2.1 : prompting user for input

name = input("Enter your name: ")
print("Hello, ", name, "!")

# Exercise 2.2 
# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). 
# You should use input to read a string and float() to convert the string to a number. 
# Do not worry about error checking or bad user data.

hours = input("Enter hours: ")
rate = input("Enter rate per hour: ")

gross_pay  = float(hours) * float(rate)
print("Gross pay: ", gross_pay)

print(int(99.6))
