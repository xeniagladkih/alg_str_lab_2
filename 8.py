from sympy import isprime, mod_inverse

def generate_keypair(bits):
    """
    Генерація ключів для криптосистеми RSA.

    Параметри:
    bits - бітова довжина ключа

    Повертає:
    public_key - відкритий ключ у вигляді кортежу (e, n)
    private_key - закритий ключ у вигляді кортежу (d, n)
    """
    # Генерація великих простих чисел p та q
    p = generate_large_prime(bits // 2)
    q = generate_large_prime(bits // 2)

    # Обчислення модуля n та функції Ейлера φ(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Вибір експоненти для відкритого ключа
    e = 65537  # Зазвичай обирається 65537, яке є простим числом та має хороші властивості

    # Обчислення секретного ключа
    d = mod_inverse(e, phi_n)

    # Повертаємо ключі
    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key

def generate_large_prime(bits):
    """
    Генерація великого простого числа з бітовою довжиною bits.

    Параметри:
    bits - бітова довжина числа

    Повертає:
    prime - велике просте число
    """
    while True:
        candidate = random.randrange(2**(bits-1), 2**bits)
        if isprime(candidate):
            return candidate

def encrypt(message, public_key):
    """
    Шифрування повідомлення за допомогою відкритого ключа.

    Параметри:
    message - повідомлення для шифрування
    public_key - відкритий ключ у вигляді кортежу (e, n)

    Повертає:
    ciphertext - зашифроване повідомлення
    """
    e, n = public_key
    ciphertext = pow(message, e, n)
    return ciphertext

def decrypt(ciphertext, private_key):
    """
    Розшифрування зашифрованого повідомлення за допомогою закритого ключа.

    Параметри:
    ciphertext - зашифроване повідомлення
    private_key - закритий ключ у вигляді кортежу (d, n)

    Повертає:
    decrypted_message - розшифроване повідомлення
    """
    d, n = private_key
    decrypted_message = pow(ciphertext, d, n)
    return decrypted_message

# Приклад використання:
import random

# Генерація ключів
bits = 1024  # Розмір ключа (можна вибрати більший розмір для більшої безпеки)
public_key, private_key = generate_keypair(bits)

# Повідомлення для шифрування
message = 42

# Шифрування повідомлення
ciphertext = encrypt(message, public_key)
print(f"Зашифроване повідомлення: {ciphertext}")

# Розшифрування повідомлення
decrypted_message = decrypt(ciphertext, private_key)
print(f"Розшифроване повідомлення: {decrypted_message}")
