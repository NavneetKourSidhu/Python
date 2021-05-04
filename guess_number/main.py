import random

def guess(x):
    random_num = random.randint(1,x)
    guess = 0
    while guess !=random_num:
        guess = int(input(f'guess a number between 1 and {x}:'))
        if guess < random_num:
            print("Too low number,give another try")
        elif guess > random_num:
            print("Too high number, take another chance")
    print(f'Congratzz, Your guess is right{random_num}!')
guess(20)            
