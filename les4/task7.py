"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа,
а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
"""


def fact(n):
    if n < 0:
        raise ValueError('факториал отрицательного числа не определен')
    elif n == 0:
        return 1
    else:
        factorial = 1
        for f in range(1, n + 1):
            factorial *= f
            yield factorial


if __name__ == "__main__":
    while True:
        n_str = input("Введите n > 0\n")
        if n_str.isdigit():
            if int(n_str) > 0:
                break
    n = int(n_str)
    for el in fact(n):
        print(el)
