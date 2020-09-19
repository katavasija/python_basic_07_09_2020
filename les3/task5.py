"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def parse_numbers(num_str):
    """
    :param num_str: string with numbers separated by ' '
    :param summ: to sum numbers
    :return: tuple(bool, summ) True if num_str contains 'q', summ of elements in string
    """
    is_end = False
    num_candidates = num_str.split(' ')
    summ = 0
    for n in num_candidates:
        if n.isdigit():
            summ = summ + float(n)
        elif n.lower() == 'q':
            is_end = True
    return is_end, summ


if __name__ == "__main__":
    total_summ = 0
    print('Введите числа для суммирования через пробел. (q - для выхода)\n')
    while True:
        num_str = input()
        is_end, summ = parse_numbers(num_str)
        total_summ += summ
        print(f'сумма чисел:{total_summ}\n')
        if is_end:
            break
