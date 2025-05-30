# exercise 1:

a = [2,5,9,0,3,5]

for i in a:
    print("The value is: ", i)

print("Finished with the loop")
print("\n")

# Result: This will print each value in the list a, one by one, followed by "Finished with the loop".

# exercise 2: 

sum = 0
for i in a :
    sum = sum + i
    print("The current sum is: ", sum)
print("The final sum is: ", sum)
print("\n")

# Result: This will calculate the sum of all values in the list a, printing the current sum after each addition, and finally printing the total sum.

# exercise 3: 

count = 0
for i in a :
    count = count + 1

print("The total count of elements in the list is: ", count)

# Result: This will count the number of elements in the list a and print the total count.
    
index = None
for i in a :
    index = count - 1
    count = count - 1
    print("The reverse value at index", index, "is:", a[index])
print("Finished with the reverse loop")