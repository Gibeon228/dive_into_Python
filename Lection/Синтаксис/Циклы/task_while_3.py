min_limit = 0
max_limit = 10
count = 3
num = None

while count > 0:
    print('Попытка ', count)
    count -=1

    print('Введите число между ', min_limit, ' и ', max_limit, '? ')
    num = float(input())
    if num < min_limit or num > max_limit:
        print('неверно')
    else:
        break

else:
    print('К сожалению все попытки исчерпаны') # else через break не работает
    quit() # функция, встроенная в пайтон 

print('Было введено число ', num)