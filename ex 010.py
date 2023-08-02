#Create a program that reads how much money a person has in their wallet and shows how many dollars they can buy
#consider US$1.00 = 3.27

n1 = float(input('How much money do you have in your wallet in Brazilian currency?'))
print('You could buy R${:.2f} dollars with this amount.'.format(n1/3.27))