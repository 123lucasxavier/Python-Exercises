#Write a program that reads any year and display whether it's a leap year

from datetime import date

year = int(input('Enter any year or enter 0 to the current year: '))

if year == 0:
    year = date.today().year

print('It\'s a leap year') if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else print('It\'s not a leap year')
