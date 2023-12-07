import random

def miller_rabin_test(n, k=5):
    """
    Алгоритм Міллера-Рабіна для перевірки числа на простоту.

    Параметри:
    n - перевіряєме число
    k - кількість ітерацій

    Повертає:
    True, якщо число n ймовірно просте
    False, якщо число n складене
    """
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n == 1:
        return False

    # Знаходження параметрів d та r для представлення n - 1 = 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Проведення k ітерацій тестування
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False  # n - складене

    return True  # n ймовірно просте

# Приклад використання:
number_to_check = 23
is_prime = miller_rabin_test(number_to_check)

if is_prime:
    print(f"{number_to_check} ймовірно просте число.")
else:
    print(f"{number_to_check} складене число.")
