#!/usr/bin/python
# author: Peter Toth
# web: ptoth.github.io
# github: github.com/ptoth


## Default Arguments Values
def say(message, times=1):
    print(message * times)


say('Hello')
say('World', 5)

## Keyword Arguments


def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)

func(3, 7)
func(25, c=24)
func(c=50, a=100)

## Return statement
'''
a return statement without a value is equivalent to 'return None'
None is like null. Represent total emptiness.
'''


def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'Equals'
    else:
        return y

print(maximum(2, 3))

print('Course-05 End')
