""" 🔁 Intermediate Loop Exercises (1 - 25)
Sum of all elements in a list -- Done ✅

Print a pattern of * in a triangle format (right-aligned) -- Done ✅

Reverse a list without using reverse() -- Done ✅

Count vowels in a string using a loop -- Done ✅

Find all prime numbers between 1 to 100 -- Done ✅

Generate Fibonacci sequence up to n terms -- Done using three methods ✅

Check if a number is prime using a loop -- Done ✅

Check if a string is a palindrome using a loop -- Done ✅

Nested loop: print multiplication table from 1 to 10 -- Done ✅

Flatten a 2D list using nested loops -- Not done ❌

Count frequency of elements in a list using a loop -- done ✅

Print elements on even positions from a list -- Not done ❌

Print numbers from 1 to 100, replacing multiples of 3 with “Fizz”, 5 with “Buzz”, and both with “FizzBuzz” -- Not done ❌

Find common elements in two lists without using set -- Not done ❌

Rotate a list k times using a loop -- Not done ❌

Find factorial using a loop -- Not done ❌

Convert a list of integers to their squares using a loop -- Not done ❌

Remove duplicates from a list using loops only -- Not done ❌

Check if two strings are anagrams (using dictionary and loops) -- Not done ❌

Calculate average, min, and max of list elements -- Not done ❌

Generate Pascal's Triangle -- Not done ❌

Transpose a matrix using nested loops -- Not done ❌

Sort a list using Bubble Sort logic -- Not done ❌

Find pairs in a list that sum to a target value -- Not done ❌

Check if a number is Armstrong using a loop -- Not done ❌

Create a pattern of numbers (e.g. pyramid, inverse pyramid) -- Not done ❌

"""

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
print("\n")
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
print("\n")
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
print("Finished with the Fibonacci sequence")
print("\n")
# Result: This will print the first 9 terms of the Fibonacci sequence, where each term is the sum of the two preceding terms, starting with 1 and 1 for the first two terms. The output will show each term along with its index in the sequence.

# Method 2: Using recursion
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
for i in range(1,10):
    print("The", i, "term", "is: ", fibonacci(i))
print("\n")
# Result: This will also print the first 10 terms of the Fibonacci sequence using a recursive function, where each term is calculated based on the two preceding terms.

# Method 3: Using a while loop

a ,b = 1, 1
n= 1
while n <= 10:
    if n == 1:
        print("The", n , "term is:", a)
    elif n==2:
        print("The", n , "term is:", b)
    else:
        c = a + b
        a = b
        b = c
        print("The", n , "term is:", c)
    n = n + 1

print("Finished with the Fibonacci sequence using while loop")
print("\n")
# Result: This will also print the first 10 terms of the Fibonacci sequence using a while loop, where each term is calculated based on the two preceding terms, starting with 1 and 1 for the first two terms.




# exercise 9:

string = "Hey this is a string in python and i am going to count the vowels in it"

vowels = "aeiouAEIOU"
spaces = " "
count_vowels = 0
count_consonants = 0
count_spaces = 0
for char in string:
    if char in vowels:
        count_vowels = count_vowels + 1
    elif char in spaces:
        count_spaces = count_spaces + 1
    else:
        count_consonants = count_consonants + 1

print("The total number of vowels in the string is: ", count_vowels)
print("The total number of consonants in the string is: ", count_consonants)
print("The total number of spaces in the string is: ", count_spaces)
print("\n")

# Result: This will count the number of vowels (both uppercase and lowercase) in the given string and print the total count.



# exercise 10:

# Method 1 : Using for loop
is_prime = True
for i in range(1, 101):
    if i < 2:
        continue
    elif i == 2:
        print(i, "is a prime number")
    else:
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i, "is a prime number")
        else:
            print(i, "is not a prime number")
        
    is_prime = True
print("\n")

# Result: This will check each number from 1 to 100 to determine if it is a prime number. It will print each prime number found, and for non-prime numbers, it will indicate that they are not prime.

# Method 2: Using a while loop
n = 1
prime = []
while n <= 100:
    if n < 2:
        n = n + 1
        continue
    elif n == 2:
        print(n, "is a prime number")
        prime.append(n)
    else:
        is_prime = True
        for j in range(2, int(n**0.5) + 1):
            if n % j == 0:
                is_prime = False
                break
        if is_prime:
            print(n, "is a prime number")
            prime.append(n)
    n = n + 1
print(prime)
print("\n")

# Result: This will also check each number from 1 to 100 to determine if it is a prime number using a while loop. It will print each prime number found and store them in a list called `prime`.



# exercise 11:

palindrome_string = input("Enter a string to check if it is a palindrome: ")
palindrome_string = palindrome_string.lower().replace(" ", "")        # Normalize the string by converting to lowercase and removing spaces
is_palindrome = True
for i in range(len(palindrome_string)):
    if palindrome_string[i] != palindrome_string[len(palindrome_string) - 1 - i]:
        is_palindrome = False
        print(f"{palindrome_string} is not a palindrome")
        break
if is_palindrome:
        print(f"{palindrome_string} is a palindrome")
print("\n")

# Result: This will check if the input string is a palindrome by comparing characters from the start and end of the string, moving towards the center. It will print whether the string is a palindrome or not.



# exercise 12:

number = int(input("Enter a number to check if it is prime: "))
number = int(number)

is_prime = True

if number < 2:
    is_prime = False

for i in range(2, int(number**0.5) + 1):
    if number % i == 0:
        is_prime = False
        break
if is_prime:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
print("\n")

# Result: This will check if the input number is prime by testing divisibility from 2 up to the square root of the number. It will print whether the number is prime or not



# exercise 13:

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print("\n")

# Result: This will print the multiplication table from 1 to 10, showing each multiplication operation in a formatted manner, with a new line after each table for clarity.



# exercise 14:


matrix1 = [2,5,3,4,6,3,4,2,7,7,3,4]

for i in range(0, len(matrix1)):
    count = 0
    for j in range(0, len(matrix1)):
        if matrix1[i] == matrix1[j] :
            count = count  + 1
    print(f"The count of element {matrix1[i]} is : {count}")
    print("\n")

# Result: This will iterate through the list `matrix1` and count how many times each element appears at its own index, printing the count for each index.

# Method 2 :

matrix1 = [2, 5, 3, 4, 6, 3, 4, 2, 7, 7, 3, 4]
already_counted = []

for i in range(len(matrix1)):
    if matrix1[i] not in already_counted:
        count = 0
        for j in range(len(matrix1)):
            if matrix1[i] == matrix1[j]:
                count += 1
        already_counted.append(matrix1[i])
        print(f"{matrix1[i]} appears {count} times\n")
