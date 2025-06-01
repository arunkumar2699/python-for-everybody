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




# exercise 3: Reverse loop
# Method 1: 
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

# Method 2: Using range
count = len(a)

for i in range(len(a) - 1, -1, -1):
    print("The reverse value at index", i, "is:", a[i])
print("Finished with the reverse loop using range")

# Result: This will also print the elements of the list a in reverse order using a range-based loop, along with their indices, and finally print "Finished with the reverse loop using range".




# exercise 4:

for i in range(10) :
    print("* " * i)

print("\n")

# Result: This will print a right-angled triangle pattern of asterisks, with each row containing an increasing number of asterisks from 1 to 9.




# exercise 5:

for i in range(10) :
    print("* " * (9-i))

print("\n")

# Result: This will print a right-angled triangle pattern of asterisks, with each row containing a decreasing number of asterisks from 9 to 1.


for i in range(1, 11):
    print(" " * (10 - i) + "* " * i)

print("\n")

# Result :  This will print a right-angled triangle pattern of asterisks, with each row containing a decreasing number of asterisks from 9 to 1, followed by another triangle with increasing asterisks from 1 to 10.

for i in range(10, 0, -1):
    print("* " * i)

# Result: This will print a right-angled triangle pattern of asterisks, with each row containing an increasing number of asterisks from 1 to 10, and then another triangle with decreasing asterisks.




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




# exercise 7:

arr1 = [1, 2, 3, 4, 5] 
arr2 = [6, 7, 8, 9, 10]
sum1 = 0
sum2 = 0
for i in arr1 :
    sum1 = sum1 + i
print("The sum of arr1 is: ", sum1)

for j in arr2 :
    sum2 = sum2 + j
print("The sum of arr2 is: ", sum2)

# Result: This will calculate the sum of all elements in arr1 and arr2 separately, printing each sum.




# exercise 8:


first_term = 1

for i in range(1,10) :
    if i == 1:
        print("The", i, "term", "is: ", first_term)
    elif i == 2:
        second_term = first_term
        print("The", i, "term", "is: ", second_term)
    else:
        next_term = first_term + second_term
        first_term = second_term
        second_term = next_term
        print("The", i, "term", "is: ", next_term)

# Result: This will print the first 9 terms of the Fibonacci sequence, where each term is the sum of the two preceding terms, starting with 1 and 1 for the first two terms. The output will show each term along with its index in the sequence.

# exercise 9:

string = "Hey this is a string in python and i am going to count the vowels in it"

vowels = "aeiouAEIOU"
count_vowels = 0
count_consonants = 0
for char in string:
    if char in vowels:
        count_vowels = count_vowels + 1
    else:
        count_consonants = count_consonants + 1

print("The total number of vowels in the string is: ", count_vowels)
print("The total number of consonants in the string is: ", count_consonants)

# Result: This will count the number of vowels (both uppercase and lowercase) in the given string and print the total count.

