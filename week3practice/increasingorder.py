#Q10 input and display integers in increasing order
num1 = int(input("Enter an integer: ")) #x
num2 = int(input("Enter another integer: ")) #y
num3 = int(input("Enter another integer: ")) #z
if num1 >= num2 and num1 >= num3: #x > y and x > z
    if num2 >= num3: #y > z
        print(f'Your numbers in increasing order are {num3}, {num2}, {num1}!') #zyx
    else: #z > y
        print(f'Your numbers in increasing order are {num2}, {num3}, {num1}!') #yzx
if num2 >= num1 and num2 >= num3: #y > x and y > z
    if num1 >= num3: #x > z
        print(f'Your numbers in increasing order are {num3}, {num1}, {num2}!') #zxy
    else: #z > x
        print(f'Your numbers in increasing order are {num1}, {num3}, {num2}!') #xzy
if num3 >= num1 and num3 >= num2: #z > y and z > x
    if num2 >= num1: #y > x
        print(f'Your numbers in increasing order are {num1}, {num2}, {num3}!') #xyz
    else: #x > y
        print(f'Your numbers in increasing order are {num2}, {num1}, {num3}!') #yxz