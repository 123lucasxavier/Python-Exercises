#Write a program that reads a number from 0 to 9999 and displays each of the digits separately.

n = int(input('Enter any number between 0 and 9999 '))

o = n // 1 % 10
t = n // 10 % 10
h = n // 100 % 10
th = n // 1000 % 10

print('Ones:', o)
print('Tens:', t)
print('Hundreds:', h)
print('Thousands:', th)

