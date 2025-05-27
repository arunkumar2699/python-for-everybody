#n = 5
#while n >= 0 :
#    print(n)
#    n = n-1
#print("Blastoff!")


# largest number in the list

for i in [9, 41, 12, 3, 74, 190, 15, 138] :
    print(i)
print("blastOff!")

largest_so_far = -1

for value in [9, 41, 12, 3, 74, 190, 15, 138] :
    if value > largest_so_far:
        largest_so_far = value
    print(largest_so_far, value)

print("The Largest value is: ", largest_so_far)

