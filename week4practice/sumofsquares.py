#Q6 ask user for integer, print sum of all square #s up to/including input
user_int = int(input('Enter a number: ')) #ask for integer X
count = 0 #set count to zero
for number in range(1, user_int + 1): #for numbers in range 1-(X+1)
    count += number ** 2 #add each number squared to count
print (count) #print final count