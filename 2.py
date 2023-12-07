from math import gcd
from sympy import mod_inverse

def chinese_remainder_theorem(congruences):
    """
    Розв'язання системи лінійних конгруентних рівнянь за модулем
    за допомогою Китайської теореми про лишки.

    Параметри:
    congruences - список кортежів (a, m), де a - залишок, m - модуль

    Повертає:
    x - розв'язок системи
    """
    M = 1  # Загальний модуль
    for _, m in congruences:
        M *= m

    result = 0
    for a, m in congruences:
        Mi = M // m
        Mi_inverse = mod_inverse(Mi, m)
        result += a * Mi * Mi_inverse

    return result % M

# Приклад використання:
congruences = [(2, 3), (3, 5), (2, 7)]
solution = chinese_remainder_theorem(congruences)
print(f"Розв'язок системи: {solution}")
