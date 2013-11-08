#!/usr/bin/python
# author: Peter Toth
# web: ptoth.github.io
# github: github.com/ptoth

## Functions


def sayHello():
    # this block belonging to this function
    print('Hello World!')
    # End of function #


def sayGoodbye():
    # this block belonging to this function
    print('GoodBye World!')
    # End of function #

sayHello()  # call the function
sayGoodbye()  # call the other function


## Functions with params
def printHigher(a, b):
    if a > b:
        print(a, 'is higher')
    elif a == b:
        print('equal')
    else:
        print(b, 'is higher')

printHigher(3, 4)  # directly give literal values

firstParam = 5
secondParam = 7
printHigher(firstParam, secondParam)  # give variables as arguments

print('Course-03 End')
