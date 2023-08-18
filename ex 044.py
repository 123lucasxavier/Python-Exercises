#Draw up a program that calculates the amount to be paid for a product, considering its normal price and payment condition:
#By cash or check: 10% off
#Credit card 1x: 5% off
#In installments 2x: normal price
#In installments 3x or +: 20% interest 

price = float(input('Please enter the product price: R$'))

payment = int(input('How would you like to pay?\nEnter\n1 - for cash or check\n2 - for credit card 1x\n3 - for 2x installments\n4 - for 3x installments or more\n'))

if payment == 1:
    print('You got 10% off, final price is R${:.2f}'.format(price - (price*0.10)))

elif payment == 2:
    print('You got 5% off, final price is R${:.2f}'.format(price - (price*0.05)))

elif payment == 3:
    print('Unfortunately you don\'t get any discount, final price is R${:.2f}'.format(price))

elif payment == 4:
    print('For the value to be divided into 3 installments or more, we add 20% to the value of the product. So the final price is R${:.2f}'.format(price + (price*0.20)))
    
else:
    print('Please, enter a number between 1 and 4.')
