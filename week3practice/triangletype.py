#Q16 determine triangle type
side1 = float(int(input('What is the length of the first side? ')))
side2 = float(int(input('What is the length of the second side? ')))
side3 = float(int(input('What is the length of the final side? ')))
if side1 == side2 or side1 == side3 or side2 == side3:
    print('You have an isosceles triangle!')
elif side1 == side2 and side2 == side3:
    print('You have an equilateral triangle!')
else:
    print('You have a scalene triangle!')