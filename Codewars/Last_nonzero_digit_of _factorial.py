def last_digit(n):
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        primfac.append(n)
    return primfac


inp = int(input('Введите число: '))
print(last_digit(inp))
# 0.05024266242980957 сек
