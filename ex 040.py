#Write a program that reads two grades from a student and calculetes the average with a final message, according to the average achieved:
#Average less than 5.0: Failed
#Average between 5.0 and 6.9: Retake
#Average 7.0 or higher: Approved

g1 = float(input('Please enter the first grade: '))
g2 = float(input('Please enter the second grade: '))

av = (g1+g2)/2

if av < 5.0:
    print('You failed! You need to study more!')
elif av >= 0.5 and av < 6.9:
    print('You must take a retake exam!')
elif av >= 7.0:
    print('You were approved! Congratulations!')