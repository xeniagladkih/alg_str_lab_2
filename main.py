def menu():
    print("Оберіть файл для виконання:")
    print("1. 1.py (Обчислення функцій Ейлера та Мьобіуса. Знаходження НСК)")
    print("2. 2.py (Розв’язання системи лінійних порівнянь за модулем)")
    print("3. 3.py (Обчислення символів Лежандра та Якобі)")
    print("4. 4.py (Алгоритм факторизації довгих цілих чисел)")
    print("5. 5.py (Алгоритм знаходження дискретного логарифма)")
    print("6. 6.py (Алгоритм Чіпполі знаходження дискретного квадратного кореня)")
    print("7. 7.py (Алгоритм перевірки чисел на простоту)")
    print("8. 8.py (Криптосистема RSA або криптосистема Рабіна)")
    print("9. 9.py (Криптосистема Ель-Гамаля над еліптичними кривими)")

def run_file(filename):
    try:
        exec(open(filename).read())
    except Exception as e:
        print(f"Помилка виконання файлу {filename}: {e}")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Введіть номер файлу (або 'exit' для виходу): ")
        
        if choice.lower() == 'exit':
            break
        
        try:
            choice = int(choice)
            if 1 <= choice <= 9:
                filename = f"{choice}.py"
                run_file(filename)
            else:
                print("Введений номер файлу недійсний. Спробуйте ще раз.")
        except ValueError:
            print("Введіть ціле число або 'exit'.")
