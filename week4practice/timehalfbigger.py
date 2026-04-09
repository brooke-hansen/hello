#Q1 determine how many times larger can be halved while still being larger than 
larger = int(input('Enter the larger number: ')) #ask for larger number
smaller = int(input('Enter the smaller number: ')) #ask for smaller number
count = 0 #set count to 0
if larger > smaller: #if larger is bigger than smaller 
    while (larger / 2) >= smaller: #while 1/2 of larger is still bigger than or equal to smaller
        larger /= 2 #divide the larger in half
        count += 1 #add 1 to count, repeat until no longer true
    print (f'that number can be halved {count} times and still be larger than {smaller}!') 