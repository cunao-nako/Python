def digital_root(n):
    while True:
        # разбиение числа на составляющие
        k = len(n)
        n = int(n)
        n = n
        number = []
        first = 100
        second = 10
        numb = n % second  # первый десяток
        number.append(numb)
        numb = n % first // second  # второй десяток
        number.append(numb)
        while (len(number) < k):  # если в числе больше 2-х десятков
            first *= 10
            second *= 10
            numb = n % first // second
            number.append(numb)
            print(number)
        number = number[::-1]
        # сложение десятков числа
        summa = sum(number)
        # проверка
        summa = str(summa)
        if len(summa) == 1:
            break
        else:
            n = summa
            continue
    return summa


a = input('Введите число: ')
print(digital_root(a))
