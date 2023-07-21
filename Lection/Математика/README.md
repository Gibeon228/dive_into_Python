# Математические модули

В Python есть несколько математических модулей в стандартной библиотеке, которе облегчают математические расчёты:

### import math (Доступ к модулю математики):

dir(math)

***Константы:*** e, inf(инфинити бесконечность), nan(not a number, не число), pi, tau

***Математические функции:*** acos, acosh, asin, asinh, atan, atan2, atanh, ceil, comb, copysign, cos, cosh, degrees, dist, erf, erfc, exp, expm1, fabs, factorial, floor, fmod, flexp, fsum, gamma, gcd, hypot, isclose, isfinite, isinf, isnan, isqrt, lcm, lgamma, log, log10, log1p, logmodf, nextafter, perm, pow, prod, radians, remainder, sin sinh, sqrt, tan, tanh, trunc, ulp 

### import decimal (Для доступа к модулю, позволяющий использовать числа с высокой точностью)

**num = decimal.Decimal(object)**
Получаем вещественное число с точностью 28 знаков(до и после запятой)

**decimal.getcontext().prec = dec** 
Задаём точность в dec знаков для будущих операций


### import fractions (Для того, чтобы работать с дробями, напрмимер 1/3)

**Запись дробей виде 1/3, 3/5  и т.д.**
f1 = fractions.Fraction(1, 3)
print(f1)

### Комплексные числа
complex([real[, imaq]]) - комплексное число из действительной real и мнимой imag частей

a = complex(2, 3)
b = complex('2+3j')

### Математические функции "из коробки"

abs(x) - возвращает абсолютное значение x, число по модулю

divmod(a, b) - вовращает пару чисел - частное и остаток от целочисленного деления. Аналогично вычислению a//b и a % b

pow(base, exp[, mod]) - при передаче 2-х аргументов возводит число base в степень exp. При передаче 3-х аргументов, результат возведения в степень делится по модулю на значение mod.

round(number[, ndigits]) - округляет число number до ndigits цифр после запятой. Если второй аргумент не передать, округляет до ближайшего целого