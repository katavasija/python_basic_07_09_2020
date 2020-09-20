"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. 
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. 
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
import sys


def calc_salary(hours, rate, bonus):
    assert hours > 0, "количество часов должно быть > 0"
    assert rate > 0, "почасовая ставка должна быть > 0"
    assert bonus >= 0, "премия должна быть >= 0"
    return (hours * rate) + bonus


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print('Usage:>python task1.py hours rate bonus')
        exit(0)
    _, hours, rate, bonus = sys.argv
    print(f'salary:{calc_salary(float(hours), float(rate), float(bonus))}')
