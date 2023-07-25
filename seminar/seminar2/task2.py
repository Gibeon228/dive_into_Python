import sys

data = [1, 5.2, "help", False, 1, '1', 'help']

for i in range(len(data)):
    item_int = "это целое число" if isinstance(data[i], int) else ''
    item_str = "это строка" if isinstance(data[i], str) else ''
    print(f'{i+1}, значение = {data[i]}, адрес в памяти: {id(data[i])}, размер памяти: {sys.getsizeof(data[i])}, хэш: {hash(data[i])}, {item_int}, {item_str}')


