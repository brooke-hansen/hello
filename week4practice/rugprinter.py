#Q11 ask for width, length, and pattern -> generate a rug consisting of pattern and dimensions
rugwidth = int(input('Enter a width: ')) #ask for how many characters wide the user wants their rug
ruglength = int(input('Enter a length: ')) #ask for how many characters tall the user wants their rug
rugpatt = input('Enter a pattern: ') #ask for what character they'd like on their rug
count = 0 #start with 0 rows
while (count != ruglength): #while the rows don't equal the ruglength
    count += 1 #add 1 (row) to the count
    print(rugpatt * rugwidth) #in the row, print the pattern by width amount of times