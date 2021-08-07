number = int(input('number: '))
sum = 0
temp = number

while temp > 0:
    cube = temp % 10
    sum += cube**3
    temp //= 10
if number == sum:
    print('armstrong number')
else:
    print('not a armstrong number')

