smallest = None
largest = None

while True :
    num = input("Enter a value: " )
    if num == 'done' :
        break
    try :
        num = int(num)
    except :
        print("Invalid input")
        continue
    
    if largest is None or num > largest:
        largest = num
    #print(largest, num)

    if smallest is None or num < smallest:
        smallest = num
    #print(smallest, num)

print("Maximum is",largest)
print("Minimum is",smallest)

