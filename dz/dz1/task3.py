# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint num = randint(LOWER_LIMIT, UPPER_LIMIT)
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1001  # Если включать 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)

print('Игра началась')
print('У вас есть 10 попыток угадать число от 0 до 1000')
print(num)
count = 10

while count > 0:
    number = int(input('Введите число: '))
    if number < num:
        print('Введённое вами число меньше загаданного')
    elif number > num:
        print('Введённое вами число больше загаданного')
    else:
        print('Вы отгадали число')
        break
    count -= 1
    print(f'Осталось попыток: {count}')
else:
    print(f' Вы не отгадали число, данное число было {num}')
