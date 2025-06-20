# Exercise 5.2 :
# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
# Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None

while True:
    num = input("Enter a value: ")
    if num == 'done':
        break
    try:
        num = int(num)
    except:
        print("Invalid Input")
        continue

    if largest is None or num > largest:
        largest = num
    print("Largest so far:", largest)

    if smallest is None or num < smallest:
        smallest = num
    print("Smallest so far:", smallest)

print("Maximum is", largest)
print("Minimum is", smallest)
