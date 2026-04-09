#Q4 function that returns list of odd numbers in a range
def output_odd(lowernum, uppernum):
    numlist = []
    oddnum = ''
    for number in range(lowernum, uppernum +1):
        if number % 2 == 1:
            oddnum = number
            numlist.append(oddnum)
            oddnum = ''
    return numlist

print(output_odd(11,21))