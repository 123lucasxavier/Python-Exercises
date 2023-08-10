#Make a program that reads the length of the legs of a right triangle, calculates and displays the lenght of the hypotenuse

import math

c1 = float(input('Enter the value of one of the legs of the triangle '))
c2 = float(input('Enter the value of other leg of the triangle '))
h = math.hypot(c1,c2)

print('The hypotenuse of this triangle equals {:.2f}'.format(h))