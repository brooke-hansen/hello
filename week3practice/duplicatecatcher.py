#Q13 determine how many of 3 user integers are copies
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
z = int(input("Enter a number: "))
samenum = 0
if x == y and x == z or y == z and y == x or z == y and z == x:
    samenum += 3
elif x == y or x == z or y == z:
    samenum += 2
if samenum > 0:
    print(f'you entered the same number {samenum} times')
else:
    print('You entered all unique numbers!')