#!/usr/bin/python
# author: Peter Toth
# web: ptoth.github.io
# github: github.com/ptoth

##List structure

#This is my list
fruits = ['apple', 'banana', 'ananas', 'lemon']
print('I have', len(fruits), 'fruits')
print('These are:')
for item in fruits:
    print(item)
print('\nI also have grapes')
fruits.append('grapes')

print('My fruits are now:') 
print(fruits)

print('I will sort them now')
fruits.sort()

print('Sorted fruit-list is')
print(fruits)

print('The first item I will eat is:')
print(fruits[0])
olditem = fruits[0]
del fruits[0]

print('I ate:')
print(olditem)

print('My fruits are now')
print(fruits)



print("\nCourse-09 End")