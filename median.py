# calculate median of a data

data = [9,7,8,3,6,4,5]

n = len(data)
for i in range(n):
    for j in range(0, n - i - 1):
        # Swap if the current element is greater than the next
        if data[j] > data[j + 1]:
            temp = data[j]
            data[j] = data[j + 1]
            data[j + 1] = temp

print(data)

