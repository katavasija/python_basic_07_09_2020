"""
Программа принимает действительное положительное число x
и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать
в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения
числа в степень.
"""


def my_func(x, y):
    """
    :param x: float > 0
    :param y: int < 0
    :return: pow(x, y)
    """
    x = float(x)
    y = int(y)
    assert x > 0, "x действительное положительное число"
    assert y < 0, "y целое отрицательное число"

    # return x ** y
    for _ in range(1, abs(y)):
        x *= x
    return 1 / x


if __name__ == "__main__":
    print(my_func(2, '-2'))
