#Write a program that reads the length of three lines of a triangle and shows whether or not they can form a triangle

line1 = float(input('Enter the first line in meters: '))
line2 = float(input('Enter the second line in meters: '))
line3 = float(input('Enter the third line in meters: '))

if line1 * line2 * line3 == 0 or line1 < 0 or line2 < 0 or line3 < 0:
    print('Please enter a positive number greater than 0')

if line1 + line2 > line3 and line1 + line3 > line2 and line2 + line3 > line1:
   print('It\'s possible to form a triangle with these lines!')
else:
   print('It\'s not possible to form a triangle with these lines!')

