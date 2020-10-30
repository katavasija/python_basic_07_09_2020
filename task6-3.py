"""
Реализовать базовый класс Worker (работник),
в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': 0, 'bonus': 0}


class Position(Worker):
    def __init__(self, position, name, surname, wage, bonus):
        assert wage > 0, 'Оклад должен быть больше 0'
        assert bonus >= 0, 'Премия должна быть не меньше 0'
        super().__init__(name=name, surname=surname, position=position)
        self._income[wage] = wage
        self._income['bonus'] = bonus

    def get_full_name(self):
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        return sum(self._income.values())


if __name__ == "__main__":
    sysadmin = Position('Системный администратор', 'jeka', 'Самохвалов', 1500, 500)
    print(sysadmin.get_full_name(), sysadmin.get_total_income())
