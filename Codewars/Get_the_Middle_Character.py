def get_middle(s):
    if (len(s) % 2 == 0):
        print('четное количество')
        symbol = int(len(s) / 2)
        print(s[symbol - 1] + s[symbol])
    else:
        print('нечетное количество')
        symbol = int(len(s) / 2)
        print(s[symbol])
    return symbol


a = input('')
get_middle(a)
