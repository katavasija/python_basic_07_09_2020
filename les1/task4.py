"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

if __name__ == '__main__':
    while True:
        number_str = input("Введите число n (>0)\n")
        if number_str.isdigit():
            if int(number_str) > 0:
                break
    max_digit = 0
    number = int(number_str)
    while number:
        digit = number % 10
        if digit > max_digit:
            max_digit = digit
        number = number // 10
    print(f"самая большая цифра в числе {number_str}: {max_digit}")
