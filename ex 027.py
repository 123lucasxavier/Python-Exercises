#Write a program that reads someone's full name, appearing next to the first and last name separately

name = (input('Type your full name: ').strip())

fn = name.split()[0]
ln = name.split()[-1]

print('It\'s nice to meet you {}\nYour first name is: {}\nAnd your last name is: {}'.format(name,fn,ln))


#also could use len(name)-1 to get the last name in strip