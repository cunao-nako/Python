def printMax(a, b):
    if a > b:
        print(a, 'больше')
    elif a < b:
        print(b, 'больше')
    else:
        print(a, 'равно', b)

printMax(2, 5)

x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
printMax(x, y)