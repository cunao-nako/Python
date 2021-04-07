# Задание 15: List Comprehension
# Из исходного списка greetings = ['hello', 'hi', 'hey', 'hola']
# создайте новый список содержащий
# вторую букву из каждой строки исходного списка.
# Выведите новый список на печать.
# Решите задание двумя способами - при помощи List Comprehension и без него.

greetins = ['hello', 'hi', 'hey', 'hola']
test_list = [item[1] for item in greetins]
test_list_1 = []
for item in greetins:
    test_list_1.append(item[1])
print(f'Список созданный с List Comprehension:\n{test_list}')
print(f'Список созданный без List Comprehension:\n{test_list_1}')

# Из исходного списка digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# создайте новый список содержащий нечетные числа исходного списка.
# Выведите новый список на печать.
# Решите задание двумя способами - при помощи List Comprehension и без него.

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_of_digits = [number for number in digits if number % 2 != 0]
print(list_of_digits)
list_of_digits_1 = []
for number in digits:
    if number % 2 != 0:
        list_of_digits_1.append(number)
print(f'Список созданный с List Comprehension:\n{list_of_digits}')
print(f'Список созданный без List Comprehension:\n{list_of_digits_1}')
