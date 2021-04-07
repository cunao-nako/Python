from fractions import Fraction

x = Fraction(1, 3)
y = Fraction(4, 6)
print(x, y)

result = x + y
print(result, type(result))

x = Fraction('1.1')
y = Fraction('2.2')
print(x, y)

result = x + y
print(result, type(result))
