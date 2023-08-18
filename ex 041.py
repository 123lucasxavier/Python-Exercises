#The national swimming federation needs a program that reads the year of birth of an athlete and show his category, according to his age
#up to 9 years: child
#up to 14 years: teenager
#up to 19 years old: junior
#up to 20 years old: senior
#over 20 years old: master

age = int(input('Hello swimmer, how old are you? '))

if age <= 9:
    print('Your category is child!')
elif age <= 14 and age > 9:
    print('Your category is teenager!')
elif age <= 19 and age > 14:
    print('Your category is junior!')
elif age <= 20 and age > 19:
    print('Your category is senior!')
elif age > 20:
    print('Your category is master!')
    