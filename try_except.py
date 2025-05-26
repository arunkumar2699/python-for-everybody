
number = input("Enter the a number: ")

try :
    number = int(number)

except:
    number = -1

if number > 0 :
    print("The number is: ", number)

else :
    print("It's not a number")

