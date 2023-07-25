import decimal
import math
from decimal import Decimal
decimal.getcontext().prec = 43
diameter = Decimal(input('Введите диаметр круга: '))

if int(diameter) > 1000:
    print("Введены некорректные значения")
else:
    print(f'Площадь круга с диаметром {diameter} равна: {Decimal(math.pi) * diameter * diameter / 4}')
    print(f'Длина окружности с диаметром {diameter} равна: {Decimal(math.pi) * diameter} ')



