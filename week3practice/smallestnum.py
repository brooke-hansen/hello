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