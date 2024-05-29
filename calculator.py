

while(True):

    firstNum = input("Enter first Number: ")
   
    if firstNum.isnumeric():
        first = float(firstNum)
        break
    else:
        print("Please enter a number")
        continue

while(True):
    secNum = input("Enter second Number: ")
    if secNum.isnumeric():
        second = float(secNum)
        break
    else:
        print("Please enter a number")
        continue

while(True):
    
    operation = input("Enter the Operation: ")
    if operation == '+':
        third = first + second
        break
    elif operation == '-':
        third = first + second
        break
    elif operation == '*':
        third = first + second
        break
    elif operation == '/':
        third = first + second
        break
    elif operation == '%':
        third = first + second
        break
    else:
        print("try again")
        continue

print(third)