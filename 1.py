def euler_phi(n):
    result = n  # Початкове значення - n
    p = 2

    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1

    if n > 1:
        result -= result // n

    return result

def mobius_mu(n):
    if n == 1:
        return 1

    factor_count = 0
    p = 2

    while n > 1:
        if n % p == 0:
            factor_count += 1
            n //= p
            if n % p == 0:
                # Якщо n має квадрат як чинник, то μ(n) = 0
                return 0
        p += 1

    # Якщо n є продуктом квадратів різних простих чисел, то μ(n) = (-1)^(кількість простих множників)
    return (-1) ** factor_count

from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_of_list(numbers):
    result = 1
    for num in numbers:
        result = lcm(result, num)
    return result

numbers = [15, 21, 35]
euler_phi_result = euler_phi(35)
mobius_mu_result = mobius_mu(35)
lcm_result = lcm_of_list(numbers)

print(f"Функція Ейлера для 35: {euler_phi_result}")
print(f"Функція Мьобіуса для 35: {mobius_mu_result}")
print(f"НСК чисел {numbers}: {lcm_result}")
