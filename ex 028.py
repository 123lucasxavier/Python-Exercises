#Write a program that makes the pc choose a random number between 0 and 5, then asks to the user guess which number was chosen. The pogram must display whether the user was right or wrong

import random

number = random.randint(0,5)

guess = str(input('Guess the number im thinkin, it\' between 0 and 5. Good Luck! '))

if guess == number:
    print('Very nice, you got it!')
else:
    print('Unfortunately it\'s wrong, better luck next time.')