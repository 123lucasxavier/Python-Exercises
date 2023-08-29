#Write a program that calculates the sum of odd numbers that are multiples of three and that are in the range from 1 to 500.

#accumulator
sum = 0

#counter
count = 0

for num in range(1, 501, 2):
   if num % 3 == 0:
        #sum = sum + num
        sum += num
        #count = count + 1
        count += 1
print('The sum of the {} numbers is {}.'.format(count, sum))