#Make a program that reads the name of a city and says whether or not it starts with the name "SANTO".

c = str(input('Enter the name of the city where you live '.capitalize())).strip()

print('Santo' in c[:5])