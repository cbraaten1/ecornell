"""
A simple die roller

Author:Connor Braaten
Date:October 31,2021
"""

import random
y=input('Type the first number: ')
z=input('Type the last number: ')
y=int(y)
z=int(z)
first=y
last=z
x=random.randint(first,last)
roll=x
print('Choosing a number between '+str(first)+' and '+str(last)+'.')
print('The number is '+str(roll)+'.')
