#Write a program that asks for an employee's salary and calculates the amount of the raise.
#For salarys over R$ 1,250.00, calculate a raise of 10%.
#For lower or equal salarys, the raise is 15%.

import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

salary = float(input('Enter your current salary: $'))

if salary > 1250.00:
    new_salary = salary + salary*0.10
else:
    new_salary = salary + salary*0.15

new_salary = locale.currency(new_salary, grouping=True)

print('Your salary is now: {}'.format(new_salary))