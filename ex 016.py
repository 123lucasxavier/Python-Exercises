#Make a program that reads any real number and displays the integer portion of the number

import math

n = float(input('Enter any non-integer number, and I will display only the integer part of this number '))

i = math.trunc(n)

print('The intenger part of {} is {}'.format(n,i))
