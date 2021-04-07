def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'Числа равны'
    else:
        return y
x=int(input('Введите первое число: '))
y=int(input('Введите второе число: '))
print('Самописная функция:', maximum(x, y))
print('Встроенная функция:', max(x, y))