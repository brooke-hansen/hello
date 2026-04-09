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