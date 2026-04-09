'''
#Q1 determine how many times larger can be halved while still being larger than 
larger = int(input('Enter the larger number: ')) #ask for larger number
smaller = int(input('Enter the smaller number: ')) #ask for smaller number
count = 0 #set count to 0
if larger > smaller: #if larger is bigger than smaller 
    while (larger / 2) >= smaller: #while 1/2 of larger is still bigger than or equal to smaller
        larger /= 2 #divide the larger in half
        count += 1 #add 1 to count, repeat until no longer true
    print (f'that number can be halved {count} times and still be larger than {smaller}!') 
'''
'''
#Q2 ask for word, print every other letter in word, starting w/ 2nd letter
userword = input('Enter a word: ') #ask for word
for letter in range(len(userword)): #for letters in the range of the length of the word
     if letter % 2 == 1: #if the letter is in an odd index position
         print(userword[letter], end = '') #print the list(letter), same line
'''
'''
#Q3 use a loop to print every even # btwn 37-1050, inclusively
for number in range(37,1050+1): #for number in range of 37-1051
    if number % 2 == 0: #if the number is even
        print(number) #print the number
'''
'''
#Q4 use a loop, calculate sum of all odd #s btwn 50-517, print results
count = 0 #set the count to zero
for number in range(50,517+1): #for number in range of 50-518
    if number % 2 == 1: #if the number is odd
        count += number #add the number to the count
print (f'The sum of all odd numbers between 50 and 517 inclusively are {count}')
'''
'''
#Q5 ask for integer, print each # that is factor of input
user_int = int(input("Enter a number: ")) #ask for integer X
print(f"The factors of {user_int} are:", end = ' ')
for number in range(1,user_int+1): #for numbers in range of 1-(X+1) 
    if user_int % number == 0: #if X / n is a whole number
        print(number, end = ' ') #print number(s) in one line
'''
''''
#Q6 ask user for integer, print sum of all square #s up to/including input
user_int = int(input('Enter a number: ')) #ask for integer X
count = 0 #set count to zero
for number in range(1, user_int + 1): #for numbers in range 1-(X+1)
    count += number ** 2 #add each number squared to count
print (count) #print final count
'''
'''
#Q7 ask user for letters until type done, then print complete word
word = "" #set word to fill-in-blank
while True: #while True loop
    letter = input("Enter a letter (or type 'done' to finish): ") #ask for letter input
    if letter == "done": #if user types done
        break #done
    word += letter #add letters to fill in blank-space word
print("Your new word is:", word) #print accumulated letters
'''
'''
#Q8 ask user for integers until neg input recieved, print sum of all input given (except for neg)
sum = 0 #set sum to 0
while True: #while True loop
    user_int = int(input('Enter an integer: ')) #ask for numbers
    if user_int < 0: #if number is less than 0
        break #done
    sum += user_int #add each integer input to sum
print(sum) #print final sum
'''
'''
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
'''
'''
#Q10 repeatedly ask for integers until neg. report back largest even or -1
largest_even = -1 #set output
while True: #while True 
    user_int = int(input("Enter a number: ")) #ask for integer
    if user_int < 0: #if the integer is less than 0
        break #done
    if user_int % 2 == 0 and user_int > largest_even: #if the integer is even and larger than set output
        largest_even = user_int #rest output to new output
print("The largest even number entered was: ", largest_even) #print output
'''
'''
#Q11 ask for width, length, and pattern -> generate a rug consisting of pattern and dimensions
rugwidth = int(input('Enter a width: ')) #ask for how many characters wide the user wants their rug
ruglength = int(input('Enter a length: ')) #ask for how many characters tall the user wants their rug
rugpatt = input('Enter a pattern: ') #ask for what character they'd like on their rug
count = 0 #start with 0 rows
while (count != ruglength): #while the rows don't equal the ruglength
    count += 1 #add 1 (row) to the count
    print(rugpatt * rugwidth) #in the row, print the pattern by width amount of times

'''
'''
#Q12 ask for two integers -> build multiplication table from input
integer1 = int(input('Enter a number: ')) #ask for number1
integer2 = int(input('Enter a number: ')) #ask for number2
count = 0 #start with 0 rows
while (count != integer1): #while there are less rows than (number1) rows
    count += 1 #add 1 to count
    print() #prints each count vertically
    for index in range(1, integer2+1): #starts at one and goes to number2
        print(f"{index*count:3.0f}", end = ' ') #prints number2 * index number horizontally
'''
'''
#Q13 ask for an integer height -> build triange of astricks with that height
height = int(input('Enter a height: ')) #ask for how many rows they'd like
count = 0 #start with 0 rows
while (count != height): #while rows don't equal desired length
    count += 1 #add 1 
    print(count*'*') #in each row, print '*' symbol {count} amount of times 
'''