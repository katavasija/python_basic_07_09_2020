"""
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника
"""

if __name__ == '__main__':
    while True:
        proceeds_str = input("Введите значение выручки p (>=0)\n")
        if proceeds_str.isdigit():
            if int(proceeds_str) >= 0:
                break
    while True:
        costs_str = input("Введите значение издержек с (>=0)\n")
        if costs_str.isdigit():
            if int(proceeds_str) >= 0:
                break

    proceeds = int(proceeds_str)
    costs = int(costs_str)
    profit = proceeds - costs

    if profit > 0:
        print("Сработали с прибылью!")
        profitability = (profit / proceeds)
        print(f"Коэффициент рентабельности:{profitability:0.3f}")

        while True:
            employees_str = input("Введите численность сотрудников (>0)\n")
            if employees_str.isdigit():
                if int(employees_str) > 0:
                    break
        employees_number = int(employees_str)
        profit_one = profit / employees_number
        print(f"Прибыль в расчете на одного сотрудника:{profit_one:0.3f}")
    elif profit == 0:
        print("Сработали в ноль!")
    else:
        print("Сработали с убытком!")
