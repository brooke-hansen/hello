#Q5 ask for integer, print each # that is factor of input
user_int = int(input("Enter a number: ")) #ask for integer X
print(f"The factors of {user_int} are:", end = ' ')
for number in range(1,user_int+1): #for numbers in range of 1-(X+1) 
    if user_int % number == 0: #if X / n is a whole number
        print(number, end = ' ') #print number(s) in one line