#class 2/3/26 - continuing from week3 branching
'''
#print all of the even numbers between 5 and 100 (inclusively)
number = 5

while number <= 100:
    if number % 2 == 0: #if number mod 2 equals 0 (if the number is divisible by 2)
        print(number)
    number = number + 1

for number in range(5,100+1):
    if number % 2 == 0:
        print(number)
'''
'''
word = 'aple'
number = 15
for letter in word:
    print(letter) #prints a p p l e
'''
'''
#count the number of 'r's in strawberry
word = "strawberry" #input word
count = 0 #set count to 0
for letter in word: #set condition: for letters in a word
    if letter == 'r': #if the letter is an r, add 1 to the count
        count += 1
print(f"the number of r's in {word} is {count}!")
'''
'''
#count the numbers of t's in the following
word = 'tastie taco time'
count = 0
for letter in word:
    if letter == 't':
        count += 1
print(f"the number of t's in {word} are {count}")
'''
'''
#suppose we have to do this a bunch of times- how to avoid copious copy/pasting
#use keyword: def --> stands for definition and signals to Python that a function is being defined
#def function_name(parameters):
    #what you want your function to do
def letter_count_in_word(word, test_letter): #when naming, start with being over specific
    count = 0
    for letter in word:
        if letter == 'test_letter':
            count += 1
    print(f"the number of {test_letter}'s in {word} are {count}")
    #This a blueprint of a function that counts 'l's inside a word

word = 'well watermelon takes swell'
letter_count_in_word(word, 'l') #inputs word and specific letter into letter_count_in_word function

word = 'tastie taco time'
letter_count_in_word(word, 't')
'''
'''
#write a function that prints the even numbers btwn a lower_bound and an upper_bound
#call that function even_printer
#call it with values 2,10 - 3,15 - 7,20
def even_printer(lower_bound, upper_bound):
    for number in range(lower_bound, upper_bound+1):
        if number % 2 == 0: 
            print(number)
        number = number + 1
even_printer(2,10)
even_printer(3,15)
even_printer(7,20)
'''
'''
#determine if the following word has the letter 'a'
word1 = "Tablespoonful"
word2 = "Technology"

a_appears = False
done = False
while not done: #using a flag

for letter in word1: #using a loop
    print(letter)
    if letter == 'a':
        a_appears = True
        done = True
        #the loop starts with the first letter
if a_appears: #if it's a, it prints.
    print(f"yes, the word {word1} has an a")
else: #if not, it moves on until it finds an a or runs out of letters
    print(f"no, the word {word1} does not have an a")
'''
#strings ---- look at ascii-code table 
#machine has a zero-based index and starts counting at 0 (humans start at 1)
'''
#indexing
word1 = "apple"
print(word1[3]) #write code to print the l
#-----------
word2 = "happy times"
print(word2[4]) #write code to print the y
print(word2[5]) #write code to print the space
print(word2[6]) #write code to print the t
print(word2[7]) #write code to print the i
print('----') #break to show difference btwn above and below
for index in range(4,7+1): #range is exclusive, solve by adding +1
    print(word2[index])

#slicing (built in syntax for indexing) ((( looks like ' [ x : y ] ' )))
print(word2[4:7]) #prints 'y t' 
print(word2[4:7+1]) #print 'y ti'
print(word2[6:10+1]) #NOT UNIVERSAL-- NOT RECCOMMENDED FOR USE OUTSIDE OF PYTHON
print(word2[6:]) #USE THIS!! THIS DEFAULTS TO GOING TO END OF STRING
'''
'''
#len - reports the length of an object (the word)
word2 = 'happy times'
print(len(word2)) #prints '11'

word = 'hello world'
for index in range(0,len(word)):
    print(index, word[index]) #prints word by letter, paired with it's 0-index position
'''

#write code to determine how many vowels are in a word 
#aeiouy
word = input("Which word would you like to check? ")
vowels = 0
for letter in word:
    if letter == 'a' or letter == 'e' or letter =='i' or letter == 'o' or letter == 'u' or letter == 'y':
        vowels += 1
print(f'You have {vowels} vowels in your word!')