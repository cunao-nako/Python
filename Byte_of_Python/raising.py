class shortInputException(Exception):
    '''Пользовательский класс исключений'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
try:
    text = (input('ВВедите что-нибудь: '))
    if len(text) < 3:
        raise shortInputException(len(text), 3)
except EOFError:
    print('Ну чо сразу EOF то?')
except shortInputException as ex:
    print('shortInputExeption: длина введёной строки - {}, ожидaлось, как минимум - {}' .format(ex.length, ex.atleast))
else:
    print('Не было исключений')