#Q6 heads or tails
from random import randint
value = randint(0,1) #picks a random integer. Either 0 or 1
user_guess = input("Heads or Tails: ") #ask user to input their guess
# 0 = Heads, 1 = Tails
if value == 0:
    print("Heads!")
    if user_guess == 'heads' or user_guess == 'Heads':
        print("Good Guess!")
    elif user_guess == 'tails' or user_guess == 'Tails':
        print("Better luck next time!")
elif value == 1:
    print("Tails!")
    if user_guess == 'tails' or user_guess == 'Tails':
        print("Correct!")
    elif user_guess == 'heads' or user_guess == 'Heads':
        print("Better luck next time!")