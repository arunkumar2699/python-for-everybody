a = 2
c = 2.0

first_name = 'Arun '
last_name = 'Gahlot'

full_name = first_name + last_name

print(full_name)

print(type(full_name))

b = '2'

print(type(b))
print(type(a))
print(type(c))

b = float(b)
print(type(b))

b = str(b)
print(type(b))

# Converting types of Data

sval = '123'
sval = int(sval)

ival = 23

add = sval + ival
print(add)

# Input name program

nam = input('Who are you? ')
print('Welcome', nam)

# US floor number conversion

inp = input('Enter Europe floor? ')
usf = int(inp) + 1
print('US floor is', usf)
