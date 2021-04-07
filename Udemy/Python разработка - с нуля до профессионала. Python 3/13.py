# Задание 13: Условный оператор if elif else
# Напишите код, который выводит сообщение: 'Enter any number'.
# Если было введено число 7,
# должно выводиться сообщение:
# '7 is a lucky number! Today is your lucky day!',
# если введено что-то другое - должно выводиться сообщение:
# 'Thank you! Have a nice day!'

number = input('Введите любое число: ')
if number == '7':
    print('7 is a lucky number! Today is your lucky day!')
else:
    print('Thank you! Have a nice day!')

# Напишите код, который выводит сообщение:
# 'Enter an integer number'
# Если было введено чётное число, должно выводиться сообщение:
# 'The number is even'14
# если было введено нечётное число, должно выводиться сообщение:
# 'The number is odd'

number = input('Введите целое число: ')
if int(number) % 2 == 0:
    print(f'{number}  - чётное')
elif int(number) % 2 != 0:
    print(f'{number} - нечётное')
