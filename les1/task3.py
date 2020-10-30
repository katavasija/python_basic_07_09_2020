"""
Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369
"""

if __name__ == '__main__':
    while True:
        number_str = input("Введите число n (>0)\n")
        if number_str.isdigit():
            if int(number_str) > 0:
                break
    double_number_str = number_str + number_str
    triple_number_str = double_number_str + number_str
    total = int(triple_number_str) + int(double_number_str) + int(number_str)
    print("сумма чисел n + nn + nnn")
    print(f"{number_str} + {double_number_str} + {triple_number_str} = {total}")
