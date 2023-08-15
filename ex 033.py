#write a program that reads 3 different number and displays which number is the biggest and which is the smallest

n1 = int(input('Hi, I\'ll tell you, between 3 numbers, which one is the biggest and which one is the smallest. Please enter the first number: '))
n2 = int(input('Enter the second number: '))
n3 = int(input('Enter the third number: '))

biggest = n1
if n2 > n1 and n2 > n3:
  biggest = n2
if n3 > n1 and n3 > n2:
  biggest = n3
  
smallest = n1
if n2 < n1 and n2 < n3:
  smallest = n2
if n3 < n1 and n3 < n2:
  smallest = n3

print ('The biggest number is {} and the smallest number is {}.'.format(biggest,smallest))