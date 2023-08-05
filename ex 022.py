#Create a program that reads a person's full name and displays:
# The name in all uppercase and lowercase letters.
# How many letters in all (not including spaces).
# How many letters are in the first name.

name = input('Enter your full name ')

print(name.upper())
print(name.lower())
print(len(name.replace(' ',"")))

s = name.split()

print(len(s[0]))