def even_or_odd(number):
    if (number % 2 == 0):
        s = 'Even'
    else:
        s = 'Odd'
    return s


a = int(input())
print(even_or_odd(a))
