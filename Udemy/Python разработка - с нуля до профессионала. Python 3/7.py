# Задание 7: Форматирование строк
# Создайте таблицу из десятичных дробных чисел
# с дробной частью разного размера.
# В таблице должно быть 4 столбца и 2 строки.
# При помощи метода format() выведите числа на экран так,
# чтобы всё число занимало 15 символов, а дробная часть 4 символа

print('{0:15.4f} {1:15.4f} {2:15.4f} {3:15.4f} \
\n{4:15.4f} {5:15.4f} {6:15.4f} {7:15.4f}'.format(12.1212121, 14.1221123, 1.3321, 5.4321,
6.232434243, 7.1212313123, 9.1212313123132, 988.1212133545))
