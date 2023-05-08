a = int(input('Введите число от 1 до 999: '))

while True:
    if 1 <= a <= 999:
        break
    a = int(input('Введите число от 1 до 999: '))

if 0 < a < 10:
    result = a ** 2
elif 10 <= a < 100:
    b = a // 10
    c = a % 10
    result = b * c
else:
    b = a // 100
    c = a % 100 // 10
    d = a % 10
    result = d * 100 + c * 10 + b
print(result)