from sympy import legendre_symbol, mod_inverse

def tonelli_shanks(n, p):
    """
    Алгоритм Чіпполі для знаходження дискретного квадратного кореня.

    Параметри:
    n - число, для якого треба знайти квадратний корінь
    p - просте число, модуль групи

    Повертає:
    x - квадратний корінь числа n за модулем p
    або None, якщо квадратний корінь не існує
    """
    # Перевірка, чи n - квадратичний залишок за модулем p
    if legendre_symbol(n, p) != 1:
        return None

    # Знаходження q та s таких, що p - 1 = q * 2^s
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1

    # Знаходження коефіцієнта z, який не є квадратичним залишком
    z = 2
    while legendre_symbol(z, p) != -1:
        z += 1

    # Ініціалізація змінних
    m, c, t, r = s, pow(z, q, p), pow(n, (q + 1) // 2, p), pow(n, q, p)

    # Головний цикл алгоритму
    while t != 1:
        i, tt = 0, (t * t) % p
        while tt != 1:
            i += 1
            tt = (tt * tt) % p

        b = pow(c, 2**(m - i - 1), p)
        m, c, t, r = i, (b * b) % p, (t * b * b) % p, (r * b) % p

    return r

# Приклад використання:
n = 7
p = 17

square_root = tonelli_shanks(n, p)

if square_root is not None:
    print(f"Дискретний квадратний корінь для {n} за модулем {p}: {square_root}")
else:
    print(f"Квадратний корінь для {n} за модулем {p} не існує.")
