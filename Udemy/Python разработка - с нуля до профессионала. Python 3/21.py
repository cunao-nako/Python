# Задание 21: Специальные (магические) методы
# Создайте класс Chain с атрибутом number_of_items. Создайте два специальных метода в этом классе.
# Первый должен при вызове встроенной функции print()
# для объекта этого класса выводить 'Chain with (значение number_of_items) items'
# Второй должен при вызове встроенной функции len()
# для объекта этого класса возвращать значение number_of_items этого объекта

class Chain:

    items = 0

    def __init__(self, name):
        self.name = name
        Chain.items += 1

    def __str__(self):
        return f'Chain with {Chain.items} items'

    def __len__(self):
        return Chain.items


x = Chain(1)
e = Chain(2)
u = Chain(3)
z = Chain(4)

print(z)
print(len(z))
