#!/usr/bin/python
# author: Peter Toth
# web: ptoth.github.io
# github: github.com/ptoth


## Local variables
x = 89


def func(x):
    print('x is', x)
    x = 102
    print('Changed local x to', x)


func(x)
print('x is still', x)


## Global variables
y = 50


def func():
    '''
        'global' refers to the variable
        which is declared outside this
        function
    '''
    global y
    print('y is', y)
    y = 102
    print('Changed global y to', y)


func()
print('Value of y is', y)

print('Course-04 End')
