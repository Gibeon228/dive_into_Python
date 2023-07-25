# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. \
# Для проверки своего кода используйте модуль fractions.
import fractions

number1 = input('Введите первую строку типа "a/b": ')
number2 = input('Введите вторую строку типа "a/b": ')
a1 = int(number1[0])
a2 = int(number2[0])
b1 = int(number1[2])
b2 = int(number2[2])

b3 = b1 * b2
a3 = a1 * b2 + a2 * b1

f1 = fractions.Fraction(1, 2)
f2 = fractions.Fraction(3, 8)
print(f1 * f2)
print(a1 * a2 / (b1 * b2))
print(a3/b3)
print(f1 + f2)
