number = 45
guess = int(input('Введите целое число: '))
if guess == number:
    print('Поздравляю, вы угадали!')
elif guess < number:
    print('Нет, загаданное число больше.')
else:
    print('Нет, загаданное число меньше.')
print('Завершенно')