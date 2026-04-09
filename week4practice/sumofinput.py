#Q8 ask user for integers until neg input recieved, print sum of all input given (except for neg)
sum = 0 #set sum to 0
while True: #while True loop
    user_int = int(input('Enter an integer: ')) #ask for numbers
    if user_int < 0: #if number is less than 0
        break #done
    sum += user_int #add each integer input to sum
print(sum) #print final sum