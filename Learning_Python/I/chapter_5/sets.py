first_set = {'A', 'B', 'C', 'D', 'E', 'F'}
second_set = {'D', 'E', 'F', 'G', 'K', 'L'}
first_operation = first_set - second_set
print('Разность first_operation и second_operation\n', first_operation)

second_operation = first_set | second_set
print('Объединение first_operation и second_operation\n', second_operation)

third_operation = first_set & second_set
print('Пересечение first_operation и second_operation\n', third_operation)

forth_operation = first_set ^ second_set
print('Симметричная разность (исключающее ИЛИ) first_operation и second_operation\n', forth_operation)

fifth_operation = [first_set > second_set, first_set < second_set]
print('Проверка на first_set надмножество second_set, first_set подмножество second_set\n', fifth_operation)

six_operation = 'A' in first_set
print('Проверка членства "A" в множестве\n', six_operation)

seven_set = set()  # создание пустого множества
seven_set.add('SPAM')  # добавление элемента в множество
seven_set.update(first_set, second_operation)  # объединение на месте
print(seven_set)
seven_set.remove('SPAM')  # удаление одного элемента
print(seven_set)


final_set = set()
my_variable = 'some string'
my_frozenset = frozenset(my_variable)  #  объект frozenset - аналог set, только анмутабельный
try:
    final_set.add({'s': 1})
except Exception as error:
    print(error)
try:
    final_set.add({1, 2})
except Exception as error:
    print(error)

final_set.add(my_frozenset)
print(final_set)
