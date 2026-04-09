#Q15 R/P/S
user1 = input("Rock, Paper, Scissors.... THROW: ")
user2 = input("Rock, Paper, Scissors.... THROW: ")
if ((user1 == 'Rock' or user1 == 'rock') and (user2 == 'Scissors' or user2 == 'scissors')) or ((user1 == 'Scissors' or user1 == 'scissors') and (user2 == 'Paper' or user2 == 'paper')) or ((user1 == 'Paper' or user1 == 'paper') and (user2 == 'Rock' or user2 == 'rock')):
    print('Player 1 wins!')
elif user1 == user2:
    print('Its a draw!')
else:
    print('Player 2 wins!')