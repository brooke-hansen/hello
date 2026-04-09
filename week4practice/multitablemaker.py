#Q12 ask for two integers -> build multiplication table from input
integer1 = int(input('Enter a number: ')) #ask for number1
integer2 = int(input('Enter a number: ')) #ask for number2
count = 0 #start with 0 rows
while (count != integer1): #while there are less rows than (number1) rows
    count += 1 #add 1 to count
    print() #prints each count vertically
    for index in range(1, integer2+1): #starts at one and goes to number2
        print(f"{index*count:3.0f}", end = ' ') #prints number2 * index number horizontally