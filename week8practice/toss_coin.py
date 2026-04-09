#Q1 function lets user guess h/t of coin toss
#default argument should be 0 for heads

from random import randint

def coin_toss(guess = 0):

    value = randint(0,1)
    if value == 0:
        print('It landed on Heads!', end = '')
    if value == 1:
        print("It landed on Tails!", end = '')
    
    if guess == value:
        return " Good guess!"
    else:
        return " Better luck next time!"
    
print(coin_toss(1))
print(coin_toss(0))
print(coin_toss())
