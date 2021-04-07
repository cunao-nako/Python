my_tuple = (0, 'one', {'two': 2})
my_tuple2 = ([3], {4, }, (5, ))
my_tuple += my_tuple2

for i in range(len(my_tuple)):
    value = my_tuple[i]
    print('Элемент кортежа №', str(i) + ':', type(value), '=', value)
