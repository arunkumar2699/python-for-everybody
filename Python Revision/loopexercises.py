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

# Result: This will print the elements of the list a in reverse order, along with their indices, and finally print "Finished with the reverse loop".

# exercise 4:

for i in range(10) :
    print("* " * i)

print("\n")
# Result: This will print a right-angled triangle pattern of asterisks, with each row containing an increasing number of asterisks from 1 to 9.
    
# exercise 5:

for i in range(10) :
    print("* " * (9-i))

print("\n")
# Result: This will print an inverted right-angled triangle pattern of asterisks, with each row containing a decreasing number of asterisks from 9 to 1.

# exercise 6:

arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 7, 8, 9, 10]
sumproduct = 0
for i in arr1:
    for j in arr2:
        product = i * j
        sumproduct = sumproduct + product
        print(f"Product of {i} and {j} is: {product}")
print("The total sum of products is: ", sumproduct)

# Result: This will calculate the product of each element in arr1 with each element in arr2, print each product, and finally print the total sum of all products.

