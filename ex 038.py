#Write a program that reads two integers and compares them, displaying a message:
#the first number is greater
#the seconrd number is greater
#both have the same value

n1 = int(input('Enter any number: '))
n2 = int(input('Enter any other number: '))

if n1 > n2:
    print('{} is greater!'.format(n1))
elif n1 < n2:
    print('{} is greater!'.format(n2))
elif n1 == n2:
    print('{} and {} are the same!'.format(n1,n2))
