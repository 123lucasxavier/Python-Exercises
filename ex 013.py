#Make an algorithm that reads an employee's salary and displays the new salary with a 15% increase

s = float(input('What is your monthly salary?'))

i = s * (15/100)

print('Your salary is now {:.2f}'.format(i + s))