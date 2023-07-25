# Напишите программу, которая получает целое число
# и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

number = int(input("Введите число: "))
str_rep = ''
print(hex(number))
while number:
    match number % 16:
        case 10:
            str_rep = 'A' + str_rep
        case 11:
            str_rep = 'B' + str_rep
        case 12:
            str_rep = 'C' + str_rep
        case 13:
            str_rep = 'D' + str_rep
        case 14:
            str_rep = 'E' + str_rep
        case 15:
            str_rep = 'F' + str_rep
        case _:
            str_rep = str(number % 16) + str_rep
    number //= 16

print(f'16_str -: {str_rep}')
