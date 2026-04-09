import math
#class practice problem 
'''
#num_units = int(input("How many units were purchased? "))
#max_num_unit = 0
#budget = 1000

#num_units = 1
#while num_units <= 1000:
    
    #if num_units <= 100:
        #price = 3.99
    #else:
        #if num_units <= 300:
            #price = 2.99
        #else:
            #price = 1.99
    #total_cost = price * num_units 
    
    #print(f'price per unit = {price}')
    #print(f'total cost = {total_cost}')
    #print(f'the cost of {num_units} is {round(total_cost,2)}')
    
    #if total_cost <= budget and num_units > max_num_unit:
        #max_num_unit = num_units

    #num_units = num_units + 1

#print(f'The max units for your budget is {max_num_unit}.')

#if num_units <= 100:
    #set_price = 3.99
#elif num_units >= 100:
    #if num_units <= 300:
        #set_price = 2.99
    #else:
        #set_price = 1.99
#print(f'Price per unit = {set_price}')
#total_cost = set_price * num_units
#print(f'total cost = {total_cost}')

#what is the point where buying more is buying less? can run program until solve, OR
'''
'''
#print all of the numbers btwn 5 and 100 (inclusively) --- use a loop
#number = 5
#while <condition>
#while number <= 100:
    #if number % 2 == 0:
        #print (number)
    #number = number + 1 #number += 1
#x = 4
#x = x + 1 #x += 1
#x = x * 2 #x *= 2

#add up all the numbers btwn 7 and 50 (inclusively)
#num = 7
#total = 0 #other variable (hand)
#while num <= 50:
    #total += num
    #num += 1
#print(f'total = {total}')

#add up all the numbers btwn 7 and 50 (exclusively)
#num = 7
#total = 0 #other variable (hand)
#while num <= 50:
    #if num % 2 == 1:
        #total += num
    #num += 1
#print(f'total = {total}')
'''
'''
#add up all odd numbers btwn 1 and 7 (exclusively)
num = 2
total = 0
while num <= 7:
    if num % 2 == 1:
        total = total + num
        num = num + 1
print(f'total = {total}')

'''

#total = 0
#for number in range (2,7):
    #if number % 2 == 1:
        #total += number
#print(f'total = {total}')

#let's ask the user for a number until they type stop. Once theyy do
#report the sum of the numbers they entered
total = 0
done = False #while loop
#for amount_of_time in range(0,100000): #limited loops
while not done: #endless loops
    user_input = input("enter a number: ")
    if user_input == 'stop':
        done = True #while loop
    else:
        user_number = int(user_input)
        total += user_number
print(f'total = {total}')

'''
#help(range)
for number in range(5,100+1):
    if number % 2 == 0:
        print(number)

for number in range (6, 100+1, 2)
'''