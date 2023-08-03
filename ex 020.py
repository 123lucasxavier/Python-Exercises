#The same teacher from the last exercise wants to raffle the order in which the students' work will be presented. Write a program that reads the name of four students and displays the order drawn.

import random

s1 = input("Enter the first student's name ")
s2 = input("Enter the second student's name ")
s3 = input("Enter the third student's name ")
s4 = input("Enter the fourth student's name ")

s = s1,s2,s3,s4
rs = random.sample (s, 4)

print('The order of the names that were drawn are {}'.format(rs))