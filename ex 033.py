#write a program that reads 3 different number and displays which number is the biggest and which is the smallest

n1 = int(input('Hi, I\'ll tell you, between 3 numbers, which one is the biggest and which one is the smallest. Please enter the first number: '))
n2 = int(input('Enter the second number: '))
n3 = int(input('Enter the third number: '))

if n1 > n2:
    if n1 > n3:
     print ('The biggest number is {}'.format(n1))
else:
    if n2 > n3:
      print('The biggest number is {}'.format(n2))
    else:
      print('The biggest number is {}'.format(n3))

if n1 > n2:
    if n2 > n3:
      print('The smallest number is {}'.format(n3))
else:
    if n1 < n3:
      print('The smallest number is {}'.format(n1))
    else:
       print('The smallest number is {}'.format(n2))
