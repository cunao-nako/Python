while True:
    s = input('Введите что-нибудь: ')
    s == 'выход'
    if s == 'выход':
        break
    elif len(s) < 3:
        print('Слишком мало')
        continue
    print('Введённая строка достаточной длины')