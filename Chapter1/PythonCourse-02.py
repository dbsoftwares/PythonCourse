#!/usr/bin/python
# author: Peter Toth
# web: ptoth.github.io
# github: github.com/ptoth

## The if statement
choice = 0
guess = int(input('Is it 0 or 1? : '))
if guess == choice:
    print('You guessed it.')  # New block starts here
else:
    print('No, you missed it...')
print('Done')
# This last statement is always executed, after the if statement is executed

## While loop
number = 15
running = True
while running:
    guess = int(input('Enter an integer : '))
    if guess == number:
        print('Congratulations, you guessed it.')
        running = False  # this causes the while loop to stop
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
else:
    print('The while loop is over.')
    # Do anything else you want to do here
print('Done')

## For loop
for i in range(1, 5):
    # range is equivalent to <code>for i in [1, 2, 3, 4]</code>
    print(i)
else:
    print('The for loop is over')

print('Course-02 End')
