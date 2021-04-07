my_set1 = {'h', 'a', 'm', 'b', 'u', 'r', 'g', 'e', 'r'}
my_set2 = {'c', 'h', 'e', 'e', 's', 'b', 'u', 'r', 'g', 'e', 'r'}

my_set = (my_set1, my_set2)
print('Tuple set\'ов:\n', my_set)

print('Пересечение set\'ов my_set1 и my_set2:\n', my_set1 & my_set2)
print('Объединение set\'ов my_set1 и my_set2:\n', my_set1 | my_set2)
print('Разность set\'ов my_set1 и my_set2:\n', my_set1 - my_set2)
print('Является ли my_set1 надмножеством my_set2:\n', my_set1 > my_set2)
print('Разность my_set2 надмножеством my_set1:\n', my_set2 > my_set1)


my_main_set = {'H', 'a', 'r', 'r', 'y', 'P', 'o', 't', 't', 'e', 'r'}
my_secondary_set = {'P', 'o', 't', 't', 'e', 'r'}
print('Является ли my_main_set надмножеством my_secondary_set:\n', my_main_set > my_secondary_set)