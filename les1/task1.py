"""
Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные,
выведите на экран.
"""

if __name__ == '__main__':
    user_name = input("Здравствуйте. Как вас зовут?\n")
    print(f"{user_name}, Вас приветствует генератор счастливых чисел в лотерее!\n")
    # low bound
    while True:
        low_bound_str = input("Введите нижнюю границу диапазона  (включительно)\n")
        if not low_bound_str.isdigit():
            print("Уточните ввод: необходимо число для нижней границы.\n")
            continue
        else:
            break
    low_bound = int(low_bound_str)

    # high bound
    while True:
        high_bound_str = input("Введите верхнюю границу диапазона\n")
        if not high_bound_str.isdigit():
            print("Уточните ввод: необходимо число для верхней границы.\n")
            continue
        else:
            if int(high_bound_str) > low_bound:
                break
            else:
                print(f"Уточните ввод: число для верхней границы должно быть больше {low_bound}\n")
                continue
    high_bound = int(high_bound_str)
    print(f"Генерация k чисел от {low_bound} до {high_bound} еще в разработке. До новых встреч!")
