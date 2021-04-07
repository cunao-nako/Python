# Задание 16: Создание функций
# Создайте функции cat_voice() and dog_voice(),
# которые выводят на экран 'Meow!' и 'Woof!' соответственно.
# Сделайте по одному вызову каждой из функций

# def cat_voice():
#     print('Meow!')


# def dog_voice():
#     print('Woof!')


# cat_voice()
# dog_voice()

# Создайте функции cat_voice() and dog_voice(),
# которые возвращают значения 'Meow!' и 'Woof!' соответственно.
# Выведите на экран 'Meow!' и 'Woof!' по 2 раза

# def cat_voice():
#     return 'Meow!'


# def dog_voice():
#     return 'Woof!'


# print(cat_voice(), cat_voice(), dog_voice(), dog_voice())

# Создайте функцию get_voice()
# которая возвращает
# передаваемый ей в качестве параметра текст c восклицательным знаком.

# def get_voice(text):
#     return text + '!'


# string = input()
# print(get_voice(string))

# Создайте функцию, которая генерирует последовательность нечетных чисел
# в диапазоне от a до b (a и b включительно),
# a и b должны передаваться в качестве параметров
# Результирующая последовательность должна возвращаться в форме объекта list.
# Решите задание двумя способами - при помощи List Comprehension и без него

def foo(a, b):
    number_list = []
    for i in range(a, b+1):
        if i % 2 != 0:
            number_list.append(i)
    return number_list


def foo1(a, b):
    number_list1 = [i for i in range(a, b+1) if i % 2 != 0]
    return number_list1


a = int(input())
b = int(input())
print(foo(a, b), foo1(a, b))
