"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта,
необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    MASSKG_1SQUAREMETER_1CENTIMETERTHICK = 25

    def __init__(self, length, width):
        assert length > 0, "длина дороги должна быть больше 0"
        assert width > 0, "ширина дороги должна быть больше 0"
        self.__length = length
        self.__width = width

    def calc_mass(self, centimeter_thick = 1):
        assert centimeter_thick > 0, "толщина полотна должна быть больше 0"
        return self.__width * self.__length * Road.MASSKG_1SQUAREMETER_1CENTIMETERTHICK * centimeter_thick


def my_float_positive_input(str_prompt):
    while True:
        input_str = input(str_prompt)
        if not input_str.isdigit():
            continue
        input_float = float(input_str)
        if input_float > 0:
            break
    return input_float


if __name__ == "__main__":
    road_length = my_float_positive_input("Введите длину дороги, м\n")
    road_width = my_float_positive_input("Введите ширину дороги, м\n")
    road_centimeter_thick = my_float_positive_input("Введите толщину покрытия, см\n")
    my_road = Road(length=road_length, width=road_width)
    print(f"Рассчитанная масса асфальта, кг:{my_road.calc_mass(road_centimeter_thick)}")
