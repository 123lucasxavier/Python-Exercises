#Write a algorithm that reads the price of a product and shows its new price, with 5% off

p = float(input('What is the price of this product?'))
d = p * 5/100

print('The discount price is R${:.2f}.'.format(p-d))