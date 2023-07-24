from decimal import Decimal as d,getcontext


print(0.1 + 0.2 == 0.3) # False
d_num = d(0.1) + d(0.2)
print(d_num) # 0.3000000000000000166533453694
# print(d_num + 3.14) # TypeError: unsupported operand type(s) for +: 'decimal.Decimal' and 'float'
print(float(d_num) + 3.14) # 3.4400000000000004
print(getcontext()) # Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[Inexact, FloatOperation, Rounded], traps=[InvalidOperation, DivisionByZero, Overflow])
getcontext().prec=2 # тоесть в значение попадет 2 цифры - 0 перед запятой не в счет
d_num = d(0.1) + d(0.2)
print(d_num) # 0.30
d_num = d(1.1) + d(0.2)
print(d_num) # 1.3
