h = int(input('Введите высоту ёлки: '))

# for i in range(h):
#     print(f'{"*"*(2*i+1):^{h*2}}') #форматирование строки

i = 0
while i < h:
    j = 0
    while j < h - 1 - i:
        print(' ', end='')
        j += 1
    j = 0
    while j < 2 * i + 1:
        print('*', end='')
        j += 1
    print()
    i += 1
