#Q4 use a loop, calculate sum of all odd #s btwn 50-517, print results
count = 0 #set the count to zero
for number in range(50,517+1): #for number in range of 50-518
    if number % 2 == 1: #if the number is odd
        count += number #add the number to the count
print (f'The sum of all odd numbers between 50 and 517 inclusively are {count}')