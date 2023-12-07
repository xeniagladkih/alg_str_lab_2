def legendre_symbol(a, p):
    """
    Обчислення символу Лежандра (a/p).

    Параметри:
    a - ціле число
    p - просте число

    Повертає:
    1, якщо a - квадратичний залишок за модулем p
    -1, якщо a - неквадратичний залишок за модулем p
    0, якщо a кратне p
    """
    if a % p == 0:
        return 0

    result = pow(a, (p - 1) // 2, p)
    return result if result == 1 else -1

def jacobi_symbol(a, n):
    """
    Обчислення символу Якобі (a/n).

    Параметри:
    a - ціле число
    n - непарне число

    Повертає:
    1, якщо a - квадратичний залишок за модулем n
    -1, якщо a - неквадратичний залишок за модулем n
    0, якщо a кратне n
    """
    result = 1
    while a != 0:
        while a % 2 == 0:
            a /= 2
            if n % 8 == 3 or n % 8 == 5:
                result = -result

        a, n = n, a
        if a % 4 == n % 4 == 3:
            result = -result
        a %= n

    return result if n == 1 else 0

a = 3
p = 11
legendre_result = legendre_symbol(a, p)
print(f"Символ Лежандра ({a}/{p}): {legendre_result}")

a = 5
n = 13
jacobi_result = jacobi_symbol(a, n)
print(f"Символ Якобі ({a}/{n}): {jacobi_result}")
