#Q13 ask for an integer height -> build triange of astricks with that height
height = int(input('Enter a height: ')) #ask for how many rows they'd like
count = 0 #start with 0 rows
while (count != height): #while rows don't equal desired length
    count += 1 #add 1 
    print(count*'*') #in each row, print '*' symbol {count} amount of times 