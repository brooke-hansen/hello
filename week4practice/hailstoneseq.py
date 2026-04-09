#Q9 print hailstone sequence starting at n=25
def hailstone_sequence(n): #def function
    number = n #set number = to later variable
    while number != 1: #while the number isn't 1
        print(number) #print number
        if number % 2 == 0: #if the number is even
            number //= 2 #divide the number in half
        else: #if the number is odd
            number = (3*number)+1 #multiply it by 3 and add 1
    print (1) #print 1 since loop above excludes it
n = 25 #set variable to 25
hailstone_sequence(n) #plug variable into function