#Write a program that reads any year and display whether it's a leap year

year = int(input('Enter any year: '))

print('It\'s a leap year') if year % 4 == 0 else print('It\'s not a leap year')
