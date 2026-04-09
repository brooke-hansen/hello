#Q10 repeatedly ask for integers until neg. report back largest even or -1
largest_even = -1 #set output
while True: #while True 
    user_int = int(input("Enter a number: ")) #ask for integer
    if user_int < 0: #if the integer is less than 0
        break #done
    if user_int % 2 == 0 and user_int > largest_even: #if the integer is even and larger than set output
        largest_even = user_int #rest output to new output
print("The largest even number entered was: ", largest_even) #print output