import random
number = random.randint(1, 100)
running = True
while running:
    guess = int(input('Введите целое число: '))
    if number == guess:
        print('Поздравляю, вы угадали!')
        running = False
    elif number < guess:
        print('Нет, загаданное число меньше.')
    else:
        print('Нет, загаданное число больше')