#Write a program that reads the speed of a car.
#If it exceeds 80km/h, show a message saying he was fined.
#The fine will cost R$7,00 for each km over the limit

import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

speed = float(input('Enter your car speed '))
fine = (speed - 80)*7
fine = locale.currency(fine, grouping=True)

if speed > 80:
    print('You were fined! It will cost {}'.format(fine))
else:
    print('Have a nice day, drive safe!')