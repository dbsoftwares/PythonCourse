#!/usr/bin/python
# author: Peter Toth
# web: ptoth.github.io
# github: github.com/ptoth

## Importing the sys module
import sys
import math

print('Your PYTHONPATH is:\n')
# referencing 'path' from the imported 'sys' module
for element in sys.path:
    print(element)
# call sqrt from undirect module
print('\nSquare root of 16 is:') 
print(math.sqrt(16))


print("\nCourse-06 End")
