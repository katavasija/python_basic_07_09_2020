"""
Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

import os
import sys

if __name__ == "__main__":
    input_str = input("Введите строку для записи в файл, нажмите Enter (пустая строка для окончания)\n")
    if len(input_str):
        lines_count = 0
        file_name = '../temp.txt'
        file_folder = os.path.dirname(__file__)

        # file full path
        # file_path = os.path.join(file_folder, file_name)
        # on nt gives me C:/Users/kot/PycharmProjects/python_basic_07_09_2020\\temp.txt
        # (on Win slash(/) as Py path separator also allowed)
        file_path = f'{file_folder}/{file_name}'
        try:
            with open(file_path, 'w') as f:
                while len(input_str):
                    f.write(f'{input_str}\n')
                    lines_count += 1
                    input_str = input()
                else:
                    print(f'Количество строк:{lines_count} записано в файл {file_path}.')
        except:
            # https://stackoverflow.com/questions/4990718/about-catching-any-exception
            print("Unexpected error:", sys.exc_info()[0])
    else:
        print('Файл не был создан.')
