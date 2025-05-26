def thing():
    print("Hello\n")
    print("Arun")

#thing()

# function for getting roots of a qaudratic equation
    
def root_of_parameter(a,b,c):
    
    import math

    a = float(a)
    b = float(b)
    c = float(c)

    D = b**2 - 4*a*c

    if D > 0:
        root1 = (-b - math.sqrt(D))/ 2*a
        root2 = (-b + math.sqrt(D))/ 2*a
        print("The discriment is: ", D)
        print("The roots are: ", root1, root2)

    elif D == 0:
        root = -b/2*a
        print("The discriment is: ", D)
        print("The root is: ", root)

    else :
        print("The discriment is: ", D)
        print("The roots are imaginary")


root_of_parameter(1,2,-3)

# Creating a language based greeting programme

def greet(lang):

    if lang == 'es' :
        print("Hola")
    elif lang == 'hi':
        print("Namaste")
    else :
        print("Hello")
    
    return "It ended"

greet('es')
greet('hi')
greet('hakuna matata')

print(greet('hi'), "Arun")






