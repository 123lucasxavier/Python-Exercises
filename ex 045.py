#Rock-Paper-Scissors game

import random

player = input('Let\'s play Rock-Paper-Scissors\nWhat you choose?\nEnter rock,  paper or scissors\n').lower().strip()

rock = 'rock'
paper = 'paper'
scissors = 'scissors'

#This function choose a single random element in a list, tuple or string
pc = random.choice([rock,paper,scissors])

#Another alternative
#plays = ('Rock','Paper','Scissors')
#pc = radiant(0,2)
#print ('The pc chose {}'.format(plays[pc]))

if pc == rock and player == rock or pc == paper and player == paper or pc == scissors and player == scissors:
    print(pc,'!')
    print('Draw! We both chose the same thing.')

elif pc == rock and player == paper or pc == scissors and player == rock or pc == paper and player == scissors:
    print(pc,'!')
    print('Well done! You won this time.')

else:
    print(pc,'!')
    print('There is! I win! Better luck next time.')
