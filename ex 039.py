from datetime import date

birth_year = int(input('Please, enter your year of birth: '))

current_year = date.today().year

age = current_year - birth_year

if age < 18:
    print('it\'s not your enlistment year yet, still {} years to go'.format(18 - age))

elif age == 18:
    print('it\'s your enlistment year! Be careful not to miss the deadline!')

elif age > 18:
    print('Your year of enlistment has passed! You are {} years late!'.format(age - 18))
