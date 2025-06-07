import math

a = int(input("Enter coefficiant of x^2: "))
b = int(input("Enter coefficiant of x^1: "))
c = int(input("Enter coefficiant of x^0: "))

D = b**2 - 4*a*c

print("Discriment is:",D)

if D > 0:
    root1 = (-b-math.sqrt(D))/2*a
    root2 = (-b+math.sqrt(D))/2*a

    print("The roots are:", root1  ,  root2)

elif D==0:
    root = -b/2*a
    print("the roots are equal and is:", root)

else:
    print("the roots are imaginary")

print("All done")

