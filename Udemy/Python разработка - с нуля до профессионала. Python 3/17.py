# Задание 17: *args. **kwargs.
# Создайте функцию is_cat_here(),
# которая принимает любое количество аргументов,
# проверяет есть ли строка 'cat' среди них.
# Функция должна возвращать True, если такой параметр есть и False в обратном случае.
# Буквы в строке 'cat' могут быть как большие, так и маленькие

def is_cat_here(*args):
    """
    Функция получает на вход tuple проверяет наличие в нём 'cat'
    :param args: tuple
    :return: True or False
    """
    my_list = []
    for item in args:
        my_list.append(item.lower())
    return ''.join(set(['True' if 'cat' in my_list else 'False' for item in my_list]))


print(is_cat_here('Dog', 'Fish', 'Lama', 'Elephant', 'Cat'))

# Создайте функцию is_item_here(item, *args),
# которая проверяет есть ли item среди args.
# Функция должна возвращать True,
# если такой параметр есть и False в обратном случае.

def is_item_here(item, *args):
    my_list = []
    for i in args:
        my_list.append(str(i))
    return ''.join(set(['True' if item in my_list else 'false' for i in args]))


symbol = input('Введите что нужно найти: ')
print(is_item_here(symbol, 'cat', 1, 2.8, 'A small sentence', True, False))

# Создайте функцию your_favorite_color()
# с позиционным параметром my_color и параметрами **kwargs,
# которая будет выводить на экран
# 'My favorite color is (значение my_color), what is your favorite color?',
# если в параметрах kwargs нет ключа color, и
# 'My favorite color is (значение my_color), but (значение по ключу color) is also pretty good!',
# если в параметрах kwargs ключ color присутствует

def your_favorite_color(my_color, **kwargs):

    if 'color' in kwargs:
        print(f'My favorite color is {my_color}, but {kwargs["color"]} is also pretty good!')
    else:
        print(f'My favorite color is {my_color}, what is your favorite color?')


color = input('Введите ваш любимый цвет: ')
your_favorite_color(color, name='Alfred', color='green')
your_favorite_color(color, name='Agna',)
