# python code of try and except and keep prompting the user for a valid number

while True:
    num = input("Enter a number: " )
    try:
        num = int(num)
        print("Number is:", num)
        break
    except:
        print("Invalid input, please enter a valid number.")
        continue
