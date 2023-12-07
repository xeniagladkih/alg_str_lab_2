def baby_step_giant_step(g, h, p):
    """
    Алгоритм "великий крок - малий крок" для знаходження дискретного логарифма.

    Параметри:
    g - генератор групи (основа системи числення)
    h - число, для якого треба знайти логарифм
    p - просте число, модуль групи

    Повертає:
    x - логарифм числа h за основою g (таке, що g^x = h mod p)
    """
    m = int(p**0.5) + 1

    # Передобчислення значень g^(m*j) для всіх j від 0 до m-1
    precomputed_values = {pow(g, j, p): j for j in range(m)}

    # Обчислення g^(-m)
    g_inv_m = pow(g, -m, p)

    # Пошук значення, що відповідає числу h в наборі {h, h*g^(-m), h*(g^(-m))^2, ..., h*(g^(-m))^(m-1)}
    for i in range(m):
        y = (h * pow(g_inv_m, i, p)) % p
        if y in precomputed_values:
            # Знайдено відповідне значення
            return i * m + precomputed_values[y]

    # Якщо немає відповідного значення
    return None

# Приклад використання:
g = 2
h = 8
p = 29

logarithm = baby_step_giant_step(g, h, p)

if logarithm is not None:
    print(f"Дискретний логарифм: {logarithm}")
else:
    print("Логарифм не знайдено.")
