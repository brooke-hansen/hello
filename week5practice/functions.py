
#ask user for two bounds and print each of the even numbers btwn those bounds inclusively
def even_printer():
    lower_bound = int(input('enter lower bound: '))
    upper_bound = int(input('enter upper bound: '))
    #blueprint of what happens when function (even_printer) occurs
    for number in range(lower_bound, upper_bound + 1):
        if number % 2 == 0: #if number mod 2 = 0 (if it's even)
            print(number)
#even_printer()
#even_printer()
#even_printer()
#even_printer()

#formal parameter:
def greeting(user_name):
    print(f"Hello {user_name}, how are you?")
    return None
#name = input('enter name: ')
#greeting(name)

def add_three(number): #name the function
    """adds 3 to a number"""
    number = number + 3 #write the function
    return number #return value after function
#x = 10 #set number
#print(x) #print number
#x = add_three(x) #rest number to value after function performed
#print(x) #print new value

def largest_value(n1, n2, n3): #compares 3 numbers and returns the largest value
    """compares 3 numbers and returns the largest value"""
    if n1 > n2:
        if n2 > n3:
            return n1
        else:
            if n1 > n3:
                return n1
            else:
                return n3
    else:
        if n1 > n3:
            return n2
        else:
            if n2 > n3:
                return n2
            else:
                return n3
#n1 = int(input('enter a number: '))
#n2 = int(input('enter a number: '))
#n3 = int(input('enter a number: '))
#print(f'the largest number entered was {largest_value(n1, n2, n3)}')


def x_in_word(word): #this function will take a word and determine if letter x is present
    """this function will take a word and determine if letter x is present"""
    for letter in word:
        if letter == "x":
            return True #immediately terminates function and returns
    return False  
#word = input('enter a word: ')
#word = x_in_word(word)
#print(word)
#help(x_in_word) #asks for help and returns either """info""" or the nearest #comment

