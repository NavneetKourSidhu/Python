import random


def play():
    user = input("Enter your choice:'r' for rock,'p' for 'paper','s' for scissor: ")
    computer = random.choice(['r','p','s'])
    # r > s, s > p , p > r
    
    if user == computer:
        return 'Its a tie -_-'
    if is_win(user,computer):
        return 'You Won :)'

    return 'You lost :('

def is_win(player,opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True 
 #   else:
 #       print("Enter a valid choice and by entering wrong choice")

print(play())         
