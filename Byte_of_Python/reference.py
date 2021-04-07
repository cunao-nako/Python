print('Простое присваивание')
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
# mylist - ещё одно имя указывающие на тот же объект
mylist = shoplist
del shoplist[0]
print('shoplist', shoplist)
print('mylist', mylist)
print('Копирование при помощи полной вырезки')
# создаём копию при помощи полной вырезки
mylist = shoplist[:]
del mylist[0]
print('shoplist', shoplist)
print('mylist', mylist)