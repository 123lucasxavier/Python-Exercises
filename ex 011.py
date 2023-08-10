#Make a program that reads the width and height of a wall in meters, calculates its area and the amount of paint needed to paint it knowing that each liter of paint paints an area of ​2m²

w = float(input('Enter the width of the wall'))
h = float(input('Enter the height of the wall'))

print('The area of this wall is {} and you will need {} liters of paint'.format((w*h),((w*h)/2)))