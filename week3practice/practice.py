'''
my_var = 
if my_var % 2 == 1:
    if my_var**3 != 27:
        my_var = my_var +4 #Assignment 1
    else:
        my_var /= 1.5 #Assignment 2
else:
    if my_var <= 10:
        my_var *= 2 #Assignment 3
    else:
        my_var -= 2 #Assignment 4
print (my_var)
'''
'''
#Q3 light color
light_color = input("Is the light red, green, or yellow: ")
if light_color == 'red':
    print("Stop")
elif light_color == 'green':
    print("Go")
elif light_color == 'yellow':
    print("Yield")
'''
'''
#Q4 Ask a user to enter 3 numbers -> determine which is largest
num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter another number: "))
num_3 = int(input("Enter another number: " ))
if num_1 <= num_2: 
    if num_2 <= num_3: 
        print(f"The larget number is {num_3}!") 
    elif num_2 >= num_3:
        print(f"The largest number is {num_2}")
elif num_2 <= num_3:
    if num_3 <= num_1:
        print(f"The largest number is {num_1}")
    elif num_3 >= num_1:
        print(f"The largest number is {num_3}")
elif num_3 <= num_1:
    if num_1 <= num_2:
        print(f"The largest number is {num_2}")
    elif num_1 >= num_2:
        print(f"The largest number is {num_1}")
'''
'''
#Q5 Ask a user to enter 3 numbers -> determine which is smallest
#OG ANSWER
num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter another number: "))
num_3 = int(input("Enter another number: " ))
if num_1 >= num_2: # n1 > n2
    if num_2 >= num_3: # n2 > n3
        print(f"The smallest number is {num_3}!") # n1 > n2 > n3
    elif num_2 <= num_3: # n2 < n3
        print(f"The smallest number is {num_2}") # n1 > n3 > n2
elif num_2 >= num_3:
    if num_3 >= num_1:
        print(f"The smallest number is {num_1}")
    elif num_3 <= num_1:
        print(f"The smallest number is {num_3}")
elif num_3 >= num_1:
    if num_1 >= num_2:
        print(f"The smallest number is {num_2}")
    elif num_1 <= num_2:
        print(f"The smallest number is {num_1}")
#EASIER SOLUTION FOUND
un1 = int(input("enter a number: "))
un2 = int(input("enter another number: "))
un3 = int(input("enter another number: "))
if un1 >= un2 and un1 >= un3:
    print(f'the largest number is {un1}')
elif un2 >= un1 and un2 >= un3:
    print(f'the largest number is {un2}')
elif un3 >= un1 and un3 >= un2:
    print(f'the largest number is {un3}')
'''
'''
#Q6 heads or tails
from random import randint
value = randint(0,1) #picks a random integer. Either 0 or 1
user_guess = input("Heads or Tails: ") #ask user to input their guess
# 0 = Heads, 1 = Tails
if value == 0:
    print("Heads!")
    if user_guess == 'heads' or user_guess == 'Heads':
        print("Good Guess!")
    elif user_guess == 'tails' or user_guess == 'Tails':
        print("Better luck next time!")
elif value == 1:
    print("Tails!")
    if user_guess == 'tails' or user_guess == 'Tails':
        print("Correct!")
    elif user_guess == 'heads' or user_guess == 'Heads':
        print("Better luck next time!")
'''
'''
#Q7 ask for a letter input --> determine if vowel or consonant 
user_letter = input("Enter a letter: ")
if user_letter == 'a':
    print("vowel")
elif user_letter == 'e':
    print("vowel")
elif user_letter == 'i':
    print("vowel")
elif user_letter == 'o':
    print("vowel")
elif user_letter == 'u':
    print("vowel")
else:
    print("consonant")
'''
'''
#Q8
customer_request = input("Pick a flavor: ")
available = False
if customer_request == 'strawberry' or customer_request == 'Strawberry':
    available = True
if customer_request == 'chocolate' or customer_request == 'Chocolate':
    available = True
if customer_request == 'vanilla' or customer_request == 'Vanilla':
    available = True
if available == False:
    print(f'{customer_request} ice cream is not available!')
else:
    print(f'Here is your {customer_request} ice cream!')
'''
'''
#Q9 user input name --> output relation
relative = input("Input name: ")
if relative == 'Darth Vader' or relative == 'darth vader':
    print('Darth Vader is your father')
elif relative == 'Leia' or relative == 'leia':
    print('Leia is your sister')
elif relative == 'Han Solo' or relative == 'han solo' or relative == 'han' or relative == 'Han':
    print('Han is your brother in law')
elif relative == 'R2D2' or relative == 'r2d2':
    print('R2D2 is your drone')
else:
    print('Unknown')
'''
'''
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
'''
'''
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
'''
'''
#Q12 HP money conversion, only print non-zero values
userk = int(input("How many knuts do you have? "))
whole_g = 0  # to be added to and then printed if >0
whole_s = 0  # to be added to and printed if >0
whole_k = 0  # to be added to and printed if >0
#convert knuts to galleons
total_g = userk / 493
whole_g = int(total_g)
#remaining knuts after galleons
remaining_knuts = userk - (whole_g * 493)
#convert remaining knuts to sickles
total_s = remaining_knuts / 29
whole_s = int(total_s)
#remaining knuts after sickles
whole_k = remaining_knuts - (whole_s * 29)
print("The smallest change you can carry is", end=" ")
first = True
if whole_g > 0:
    print(whole_g, "galleon(s)", end="")
    first = False
if whole_s > 0:
    if not first:
        print(" and ", end="")
    print(whole_s, "sickle(s)", end="")
    first = False
if whole_k > 0:
    if not first:
        print(" and ", end="")
    print(whole_k, "knut(s)")
'''
'''
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
'''
'''
#Q14 highway existence and direction
userhw = int(input('Which highway are you looking up?'))
number = userhw
#1-99 PIHW O N/S E E/W; 100-999 AHTP, N(XX) -- XX indicate which PIHW
for number in range(1,99+1):
    if number % 2:
        print(
'''
'''
#Q15 R/P/S
user1 = input("Rock, Paper, Scissors.... THROW: ")
user2 = input("Rock, Paper, Scissors.... THROW: ")
if ((user1 == 'Rock' or user1 == 'rock') and (user2 == 'Scissors' or user2 == 'scissors')) or ((user1 == 'Scissors' or user1 == 'scissors') and (user2 == 'Paper' or user2 == 'paper')) or ((user1 == 'Paper' or user1 == 'paper') and (user2 == 'Rock' or user2 == 'rock')):
    print('Player 1 wins!')
elif user1 == user2:
    print('Its a draw!')
else:
    print('Player 2 wins!')
'''
'''
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
'''
'''
#Q17 inform user of desired heart rate based on age/athleticism 
userage = int(input('Enter your age: '))
usermove = input('Do you have an above or below average athleticism? ')
'''