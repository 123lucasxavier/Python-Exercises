#Write a program that asks for the distance of a trip in km. Then calculate ticket price, charging R$ 0,50 per km for trips of up to 200km and R$ 0,45 for longer trips.

distance = int(input('Enter travel distance in km: '))

if distance > 200:
    fare_amount = 0.50
else:
    fare_amount = 0.45

ticket_price = distance * fare_amount

print('The price of your ticket will be: R${:.2f}'.format(ticket_price))