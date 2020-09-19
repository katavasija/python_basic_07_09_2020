"""
Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    """
    :param a:
    :param b:
    :param c:
    :return: sum of two without the least
    """
    def my_max(*args):
        m = float("-inf")
        for el in args:
            if el > m:
                m = el
        return m

    return my_max((a + b), (a + c), (b + c))


if __name__ == "__main__":
    print(my_func(4, 6, 5))

