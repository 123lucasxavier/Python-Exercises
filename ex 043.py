#Develop a logic that reads the weight and height  of a person, calculates its IMC and displays its stats, acording with the following table:
# - Under 18.5: Underweight
# - Between 18.5 and 25: Ideal weight
# - 25 to 30: Overweight
# - 30 to 40: Obesity
# - Over 40: Morbidly obese

weight = float(input('What is your weight in kg? '))
height = float(input('What is your height in meters? '))

imc = weight/height**2

if imc < 18.5:
    print('You are underweight!')
elif imc < 25 and imc >= 18.5:
    print('You are at the ideal weight!')
elif imc < 30 and imc >= 25:
    print('You are overweight!')
elif imc < 40 and imc >= 30:
    print('You are obese!')
elif imc >= 40:
    print('You are morbidly obese!')
    

