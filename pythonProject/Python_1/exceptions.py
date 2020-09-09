import sys

try:
    x=int(input('x: '))
    y=int(input('y: '))
except ValueError:
    print('Cannot convert a String type into an Integer type')
    sys.exit(1)


try:
    result = x/y
except ZeroDivisionError:
    print('Error cannot divide by 0.')
    print('If program throws an error then it will not continue the code becaus eof sys.exit(1), "1" is an error code.')
    sys.exit(1)



