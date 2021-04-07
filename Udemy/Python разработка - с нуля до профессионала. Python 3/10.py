# Задание 10: Tuples
# Создайте объект tuple, описывающий компьютер
# и распакуйте его в соответствующие переменные.
# Выведите переменные вызвав функцию print() один раз

my_computer_tuple = ('MacBook Pro 13\'', '2019', '1,4 GHz Intel Core i5',
                     'ГБ 2133 MHz LPDDR3',
                     'Intel Iris Plus Graphics 645 1536 МБ',
                     '1736$', '1361$')
computer_model, release_date, cpu, ram, graphics, realease_cost, nowadays_cost = my_computer_tuple
print(computer_model, release_date, cpu,
      ram, graphics, realease_cost, nowadays_cost)
