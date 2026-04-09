#Q11 input and display integers in decreasing order
x = int(input("Enter an integer: "))
y = int(input("Enter another integer: "))
z = int(input("Enter a third integer: "))
if x >= y and x >= z:
    if y >= z:
        print(f'Your numbers in decreasing order are {x}, {y}, {z}!')
    else:
        print(f'Your numbers in descending order are {x}, {z}, {y}!')
if y >= x and y >= z:
    if x >= z:
        print(f'Your numbers in descending order are {y}, {x}, {z}!')
    else:
        print(f'Your numbers in descending order are {y}, {z}, {x}!')
if z >= x and z >= y:
    if x >= y:
        print(f'Your numbers in descending order are {z}, {x}, {y}!')
    else:
        print(f'Your numbers in descending order are {z}, {y}, {x}!')