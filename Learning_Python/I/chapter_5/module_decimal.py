import decimal


print('До объявления точности\n',
      decimal.Decimal(0.1) + decimal.Decimal(0.01))
decimal.getcontext().prec = 4
print('После объявления точности\n',
      decimal.Decimal(0.1) + decimal.Decimal(0.01))

with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))
