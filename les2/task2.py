"""
Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input()
"""

if __name__ == "__main__":
    user_list = input('введите элементы списка через запятую\n')
    my_list = user_list.split(',')
    max_idx = len(my_list) - 1
    for idx in range(0, max_idx, 2):
        # change element on even index position with next element
        my_list[idx], my_list[idx + 1] = my_list[idx + 1], my_list[idx]
    print(my_list)
