import sys
try:
    x = int(input('x: '))
    y = int(input('y: '))
except ValueError:
    print('You can not divison by a string')
    sys.exit(1)
try:
    print(f'{x} / {y} = {x / y}')
except ZeroDivisionError:
    print('Can not division by zero')
    sys.exit(1)