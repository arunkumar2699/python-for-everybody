# Searching For a line in a file

# Prompting to user until the file name is acceptable.......... if you want to quit when file name is not acceptable then just
# ..... use quit() in except 

while True :

    fname = input("Enter file name: ")

    try :
        fhand = open(fname)
    except :
        print("The file is invalid")
        continue

    if True :
        fhand = open(fname)
        break


for line in fhand :
    line = line.rstrip()
    if  '@uct.ac.za' in line and line.startswith("From:"):
        print(line)  





 
