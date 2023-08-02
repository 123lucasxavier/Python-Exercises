#Information about the typed variable
x = input('Type anything: ')

print('The primitive type of this is: ', type(x))
print('Just spaces? ', x.isspace())
print('Is it a number? ', x.isnumeric())
print('Is it alphabetical? ',x.isalpha())
print('Is it alphanumeric? ',x.isalnum())
print('Is it lowercase? ',x.islower())
print('Is it uppercase? ',x.isupper())
print('Is it capitalized? ', x.istitle())
