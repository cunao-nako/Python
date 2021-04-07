import getpass


class Book:

    adressbook = {}

    def __init__(self, name, telephone):
        self.name = name
        self.telephone = telephone
        Book.adressbook[name] = telephone
        print('_' * 60, '\n')
        print('Контакт {} - создан' .format(self.name))
        print('_' * 60, '\n')


def addite():
    while True:
        print('_' * 60, '\n')
        name = input('Введите имя: ')
        print('_' * 60, '\n')
        telephone = input('Введите номер телефона: ')
        print('_' * 60, '\n')
        Book(name, telephone)
        print('_' * 60, '\n')
        var = getpass.getpass('Продолжить ввод? (1) | Закончить ввод? (2) ')
        print('_' * 60, '\n')
        if var == '1':
            continue
        elif var == '2':
            break


def delate():
    while True:
        print('_' * 60, '\n')
        name = input('Введите имя контакта, который нужно удалить: ')
        print('_' * 60, '\n')
        if name in Book.adressbook:
            del Book.adressbook[name]
        elif name not in Book.adressbook:
            print('Данного контакта не существует')
            print('_' * 60, '\n')
        print('_' * 60, '\n')
        var = getpass.getpass('Продолжить удаление? (1) | Закончить удаление? (2) ')
        print('_' * 60, '\n')
        if var == '1':
            continue
        elif var == '2':
            break
print('_' * 60, '\n')
print('Добро пожаловать в программу "Адрессная книга"!')
print('_' * 60, '\n')
print('_' * 60, '\n')
print('Для получения справки введите "help".')
print('_' * 60, '\n')
print('_' * 60, '\n')
print('Для моментального выхода из программы введите "Cntrl + C"!')
print('_' * 60, '\n')
while True:
    var = getpass.getpass('Выберите действие: добавить контакт (1) | удалить контакт (2) | выйти из программы (3) ')
    if var == '1':
        addite()
    elif var == '2':
        delate()
    elif var == '3':
        break
    else:
        print('Неизвестная команда')
file = open('adressbook.txt', 'w')
file.write(str(Book.adressbook))
print('_' * 60, '\n')
print('До свидания!')
print('_' * 60, '\n')
print(Book.adressbook)