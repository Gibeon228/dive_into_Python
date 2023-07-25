def convert(number: int, base: int) -> str:
    str_rep = ''
    while number:
        str_rep = str(number % base) + str_rep
        a // base
    return str_rep


number = int(input("Введите число: "))

a = number
str_rep = ''
while a:
    str_rep = str(a % 2) + str_rep
    a //= 2
print(f'binary_str -: {str_rep}')

a = number
str_rep = ''
while a:
    str_rep = str(a % 8) + str_rep
    a //= 8
print(oct(number))
print(f'eigth_str -: {str_rep}')

a = number
str_rep = ''
while a:
    if a % 16 == 10:
        str_rep = 'A' + str_rep
    elif a % 16 == 11:
        str_rep = 'B' + str_rep
    elif a % 16 == 12:
        str_rep = 'C' + str_rep
    elif a % 16 == 13:
        str_rep = 'D' + str_rep
    elif a % 16 == 14:
        str_rep = 'E' + str_rep
    elif a % 16 == 15:
        str_rep = 'F' + str_rep
    else:
        str_rep = str(a % 16) + str_rep
    a //= 16
print(f'eigth_str -: {str_rep}')
