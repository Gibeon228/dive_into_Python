a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

d = complex(b ** 2 - 4 * a * c, 0)

x1 = (-b + d ** 0.5) / (2 * a)
x2 = (-b - d ** 0.5) / (2 * a)

print(x1, x2, d)
