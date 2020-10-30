"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce()
"""
import functools

if __name__ == "__main__":
    # define list of even numbers [100,...,1000]
    even_numbers = [itm for itm in range(100, 1001) if not itm & 1]
    print(functools.reduce(lambda a, b: a * b, even_numbers))
