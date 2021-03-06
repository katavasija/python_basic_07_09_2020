"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
from itertools import cycle, count
from time import sleep

if __name__ == "__main__":
    # iterator from 3 to 10
    for el in count(3):
        if el > 10:
            break
        else:
            print(el)

    # cycle list
    cycle_list = ['A', 'B', 'C', 'D', 'E']
    tick_timer = 0
    for el in cycle(cycle_list):
        if tick_timer > 20:
            break
        print(el, end='')
        tick_timer += 1
        sleep(0.5)
