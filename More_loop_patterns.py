# finding a value in a list

for value in [5,6,3,64,3,64,3,65] :
    found = False
    if value == 3 :
        found = True
    print(found, value)


# Sum of a list using while loop

a = [5,6,5,8]
print(a[0])
index = 0
sum = 0
while index < len(a) :
    sum = sum + a[index]
    index = index + 1

print('The Sum is:', sum)






