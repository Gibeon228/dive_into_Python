data = 42
print(isinstance(data, int))

data = True
print(isinstance(data, int)) # логический тип подкласс инта

data = 3.14
print(isinstance(data, (int, float, complex))) # проверяет принадлежность к тому или иному классу или созданному ему под классу