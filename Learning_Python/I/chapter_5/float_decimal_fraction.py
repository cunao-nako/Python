from decimal import Decimal
from fractions import Fraction

number_one = 0.1 + 0.1 + 0.1 - 0.3
print('number_one =', number_one, type(number_one))

number_two = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
print('number_two =', number_two, type(number_two))

number_three = Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10)
print('number_three =', number_three, type(number_three))
