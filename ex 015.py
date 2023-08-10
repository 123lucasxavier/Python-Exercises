#Make a program that asks for the number of kilometers driven by a rented car and the number of days it was rented. Calculate the price to pay, knowing that the car costs $60,00 per day and $0,15 per km traveled

km = int(input('Enter the number of kilometers driven'))
d = float(input('How long, in days, did you rent the car?'))
p = km*0.15 + d*60.00

print('The amount to be paid is: R${:.2f}'.format(p))