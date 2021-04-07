# Проверка на палиндромность:
# def check(string):
#     storage = [symbol.lower() for symbol in string if symbol != ' ']
#     if storage == storage[::-1]:
#         return f'{string} - палиндром'
#     else:
#         return f'{string} - не палиндром'
#
#
# s = input('Введите слово или строку для проверки на палиндромность: ')
# print(check(s))


# Генератор строк для заполнения словаря:
# number = input('Введите числа используя пробел: ').split()
# my_dictionary = {int(item): int(item)*2 for item in number}
# print(my_dictionary)


# Генератор строк для перезаписи словаря:
# my_dictionary = {'1': 1, '2': 2, '3': 3}
# test_dictionary = {key: value*2 for key, value in my_dictionary.items()}
# print(test_dictionary)


# # Генератор строк для создания множества:
# my_list = (1, -2, 5, -3)
# my_set = {number * -1 for number in my_list}
# print(my_set)

# my_set = {letter for letter in 'Привет, как у тебя дела?'}
# print(my_set)


# Вложенный цикл для смайликов:
# string = ''
# for i in range(2):
#     string += '\U0001f600'
#     print(string)
#     for j in range(4):
#         string += '\U0001f600'
#         print(string)
# аналог с умножением строк
# for i in range(1, 11):
#     print('\U0001f600' * i)


# Функция map():
# def test_function(x):
#     x **= 2
#     return x
#
#
# number_list = [-1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
# number_list = list(map(test_function, number_list))
# print(number_list)


# Функция filter():
# def test_function(x):
#     return x % 2 == 1
#
#
# number_list = [-1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
# number_list = list(filter(test_function, number_list))
# print(number_list)


# lambda выражения:
# s = ['apple', 'Abraham', 'Bob', 'banana', 'Cris', 'cherry']
# print(sorted(s, key=lambda word: word.casefold()))


# OOP:
# class MyFirstClass:
#     pass
#
#
# my_first_object = MyFirstClass()
# print(type(my_first_object))


# Модули