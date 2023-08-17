#Write a program to approve the bank loan for the purchase of a house. The program will ask the price of the house, the buyer's salary and in how many years he will pay.
#Calculate the amount of each monthly installment, knowing that it cannot exceed 30% of the salary or else the loan will be denied

import locale
locale.setlocale(locale.LC_ALL, '')

print ('Hi, how are you? Let\'s check if whether or not you are eligible for this loan')

house_price = float(input('Please enter the value of the house you would like to buy: '))

#Turning the number into a dollar formatted string using f-string
#house_price = f"${house_price:.2f}"

monthly_salary = float(input('Whats is your monthly salary? '))

years_to_pay = int(input('In how many years you would like to pay this house? '))

print('To pay off the house in {} years the amount of the installment will be {:.2f}.'.format(years_to_pay,(house_price//(years_to_pay*12))))

if house_price//(years_to_pay*12) > monthly_salary*0.3:
    print('Unfortunately your loan was denied.')
    
else:
    print('Congratulations, your loan was approved!')

