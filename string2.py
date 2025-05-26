# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")

try :
    fhand = open(fname)

except :
    print("Invalid File")
    quit()

x = 0
count = 0

for line in fhand:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    start = line.find(' ')
    float_string = line[start + 1 : ]
    float_int = float(float_string)

    x = float_int + x
    count = count + 1


print("Average spam confidence:", x / count)





