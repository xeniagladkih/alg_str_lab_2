from math import gcd
from random import randint

def pollards_rho(n):
    """
    Факторизація числа n за допомогою ро-алгоритму Полларда.

    Параметри:
    n - ціле число, яке потрібно факторизувати

    Повертає:
    p - один із простих множників n
    """
    def f(x):
        return (x ** 2 + 1) % n

    x, y, d = 2, 2, 1

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)

    return d

# Приклад використання:
number_to_factorize = 5959
factor = pollards_rho(number_to_factorize)

print(f"Число {number_to_factorize} розкладається на множники: {factor} * {number_to_factorize // factor}")
