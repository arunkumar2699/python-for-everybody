# 1. Check if three given numbers form a Pythagorean triplet.
# 2. Determine if a given year is a leap year using nested conditionals.
# 3. Find the median of three integers using conditionals.
# 4. Check if a number is both a perfect square and a perfect cube.
# 5. Compare two strings lexicographically using if-else conditions.
# 6. Identify if a character is a vowel, consonant, digit, or special character.
# 7. Check if a number is divisible by 3 and 5 but not by 7.
# 8. Determine the maximum of four numbers using conditional logic.
# 9. Verify if a number lies within a specific inclusive range.
# 10. Validate time input in the format hours:minutes:seconds.

# 11. Check if one of two numbers is a multiple of the other.
# 12. Determine the quadrant of a point (x, y) in the Cartesian plane.
# 13. Simulate a login system with 3 attempts using conditional checks.
# 14. Categorize a number based on even/odd and its value relative to 50.
# 15. Classify a triangle as equilateral, isosceles, or scalene based on side lengths.

# 16. Simulate ATM withdrawal logic considering balance and daily limits.
# 17. Implement basic elevator control logic (floor selection, emergency stop).
# 18. Categorize a person’s age into child, teen, adult, or senior citizen.
# 19. Assign grades (A-F) based on numerical marks using conditional statements.
# 20. Simulate a traffic light system and output the allowed actions.

# 21. Determine whether a given number is prime using conditional checks.
# 22. Given a date, determine the current season (spring, summer, etc.).
# 23. Check if a given year contains 53 weeks.
# 24. Check if the sum of digits of a number is even or odd.
# 25. Implement a simple calculator with basic operations using if-elif statements.

# 26. Convert time from 24-hour format to 12-hour format using conditionals.
# 27. Determine the number of days in a month using only if-elif-else.
# 28. Check if two given times fall within the same hour.
# 29. Verify if a given date (dd, mm) is valid, considering leap years.
# 30. Check whether a date falls on a weekday or a weekend.

# 31. Validate password strength by checking character requirements.
# 32. Check if a string is a palindrome using conditional logic.
# 33. Detect if a sentence is a question by checking if it ends with '?'.
# 34. Check whether a string starts and ends with the same character.
# 35. Check if a string contains any digits or is purely alphabetic.

# 36. Compare mean and median of a list of numbers using conditionals.
# 37. Verify if all elements in a list are unique.
# 38. Check if a dictionary contains a specific key-value pair.
# 39. Determine whether a list is sorted in ascending or descending order.
# 40. Check if two lists share at least one common element.

# 41. Determine driving eligibility based on age and medical condition.
# 42. Simulate a login system with both password and OTP verification.
# 43. Create a ticket pricing logic based on age, time, and seat category.
# 44. Apply discounts in a shopping cart based on purchase amount.
# 45. Calculate final discount using flags: has_discount, is_member, is_first_time.

# 46. Assign letter grades with +/- based on score using nested conditions.
# 47. Simulate quiz scoring with partial credit and negative marking.
# 48. Suggest spelling corrections based on common verb endings like 'ing', 'ed'.
# 49. Give clothing advice based on temperature and humidity values.
# 50. Simulate a chatbot that responds differently to greetings, questions, and farewells.


# 1. Check if three given numbers form a Pythagorean triplet.

base = int(input("Enter the value of base: "))
perpendicular = int(input("Enter the value of perpendicular: "))
hypoteneous = int(input("Enter the value of hypoteneous: "))

if (hypoteneous ** 2 == perpendicular **2 + base **2) :
    print("It's a pythagorean triplet")
else :
    print("Not a pythagorean triplet")




# 2. Determine if a given year is a leap year using nested conditionals.

year = int(input("Enter the year: " ))

if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("It's a leap year")
        else:
            print("Not a leap year")
    else:
        print("It's a leap year")
else:
    print("Not a leap year")


# 3. Find the median of three integers using conditionals.

length_of_array = int(input("length of the array is: "))
array = []
for i in range(length_of_array) :
    value = int(input(f"the value of {i}th element is: " ))
    array.append(value)

print(array)
'''
if length_of_array == 3:
    if (array[0] >= array[1] and array[0] <= array[2]) or (array[0] <= array[1] and array[0] >= array[2]):
        print(f"The median is {array[0]}")
    elif (array[1] >= array[0] and array[1] <= array[2]) or (array[1] <= array[0] and array[1] >= array[2]):
        print(f"The median is {array[1]}")
    else:
        print(f"The median is {array[2]}")
elif length_of_array == 2:
    if array[0] > array[1]:
        print(f"The median is {array[0]}")
    else:
        print(f"The median is {array[1]}")
elif length_of_array == 1:
    print(f"The median is {array[0]}")
else:
    print("Invalid length of array. Please enter a length of 1, 2, or 3.")
'''

# sorting the array to find the median using for loop

for i in range(length_of_array):
    for j in range(i + 1, length_of_array):
        if array[i] > array[j]:
            array[i], array[j] = array[j], array[i]

print(array)