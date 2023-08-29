#Make a program that reads any integer and displays its table on the screen

number = int(input('Please enter any integer number: '))

for table in range(0,11):
    print('{} x {} = {}'.format(number,table,number*table))