#Make a program that reads a sentence and displays:
#How many times the letter "A" appears
#In what position does it appear for the first time
#In what position does it appear for the last time

sentence = str(input('Type a sentence: ')).strip()
a1 = sentence.lower().count('a')
a2 = sentence.lower().find('a') + 1
a3 = sentence.lower().rfind('a') + 1

print('Analyzing your sentence it can be said that the letter "A" appears {} times.\nIt appears at the position {} for the first time\nAnd appears at the position {} for the last time'.format(a1, a2, a3))
