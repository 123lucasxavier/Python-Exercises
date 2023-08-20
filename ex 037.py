#Write a program that reads an integer and asks the user what the conversion base will be, binary, octal or hexadecimal.

integer = int(input('Please enter a integer: '))

conversion_base = int(input('''What will be the basis of conversion?
Enter:
[1] for binary
[2] for octal
[3] for hexadecimal
'''))

if conversion_base == 1:
    print('The number {} in binary is {}'.format(integer,bin(integer)))
elif conversion_base == 2:
    print('The number {} in octal is {}'.format(integer, oct(integer)))
elif conversion_base == 3:
    print('The number {} in hexadecimal is {}'.format(integer, hex(integer)))
else:
    print('Please, enter a valid number: ')


