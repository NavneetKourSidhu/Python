import random


def play():
    user_input = int(input("User choice: "))
    user = input("Enter your choice:\n1. Rock\n2. Paper\n3. Scissor ")
    computer = random.choice(['r','p','s'])
    ## r > s, s > p , p > r
    
    if user == computer:
        return 'Its a tie -_-'
    if user_win(user,computer):
        return 'You Won :)'

    return 'You lost :('

def user_win(user,computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True 
    else:
        print("Enter a valid choice and by entering wrong choice")

print(play())         
