def printMax(x, y):
    '''Выводит максимальное из двух чисел.
    
Оба значения должны быть целыми числами.'''
    x = int(x) #конвертируем в целые, если возможно
    y = int(y)

    if x > y:
        print(x, ' наибольшее')
    else:
        print(y, ' наибольшее')
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
printMax(a, b)
print(printMax.__doc__)