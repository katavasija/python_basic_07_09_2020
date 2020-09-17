"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
"""

if __name__ == "__main__":
    n = 8
    lower_range_bound = 1
    high_range_bound = 8
    my_range_list = []

    print(f'введите {n} оценок от {lower_range_bound} до {high_range_bound}')
    for i in range(1, n + 1):
        while True:
            # define i-th mark
            str_i = input(f'Введите оценку №{i}\n')
            if str_i.isdigit():
                if 1 <= int(str_i) <= 8:
                    mark = int(str_i)
                    break
        # define mark place
        mark_inserted = False
        for idx in range(len(my_range_list)):
            if my_range_list[idx] < mark:
                my_range_list.insert(idx, mark)
                mark_inserted = True
                break
        if not mark_inserted:
            my_range_list.append(mark)
    print(my_range_list)
