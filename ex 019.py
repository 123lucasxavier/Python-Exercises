#A teacher wants to draw one of his four students to erase the blackboard. make a program that helps him, reading their name and writing the name of the chosen one

import random

s1 = input("Enter the first student's name ")
s2 = input("Enter the second student's name ")
s3 = input("Enter the third student's name ")
s4 = input("Enter the fourth student's name ")

s = [s1,s2,s3,s4]
rs = random.choice(s)

print('The chosen student was {}'.format(rs))