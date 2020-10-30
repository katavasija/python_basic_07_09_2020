"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""


class Car:
    SPEED_INCREMENT = 10
    DIRECTION_LEFT = 'налево'
    DIRECTION_RIGHT = 'направо'

    def __init__(self, color, name, is_police = False):
        self.color = color
        self.name = name
        self.is_police = is_police
        self._speed = 0

    def go(self):
        self._speed += Car.SPEED_INCREMENT
        self.show_speed()

    def stop(self):
        self._speed = 0
        print(f'Машина остановилась')

    def breaks(self):
        if self._speed > 0:
            self._speed -= Car.SPEED_INCREMENT
        self.show_speed()

    def show_speed(self):
        print(f'Машина едет со скоростью {self._speed}')

    def turn(self, direction):
        assert direction in (Car.DIRECTION_LEFT, Car.DIRECTION_RIGHT), f'Недопустимое направление поворота:{direction}'
        print(f'Машина повернула {direction}')


class TownCar(Car):
    def __init__(self, color, name):
        super().__init__(color=color, name=name, is_police=False)
        self.max_speed = 200
        self.town_speed_limit = 60

    def show_speed(self):
        if self._speed > self.town_speed_limit:
            print('Осторожно! Превышение скоростного режима')
        super().show_speed()


class SportCar(Car):
    def __init__(self, color, name):
        super().__init__(color=color, name=name, is_police=False)
        self.max_speed = 300
        self.speed_limit = 60

    def go(self):
        self._speed += 2 * Car.SPEED_INCREMENT
        self.show_speed()


class WorkCar(Car):
    def __init__(self, color, name):
        super().__init__(color=color, name=name, is_police=False)
        self.max_speed = 45
        self.speed_limit = 40

    def go(self):
        self._speed += Car.SPEED_INCREMENT
        if self._speed > self.max_speed:
            self._speed = self.max_speed
        print(f'Трактор едет со скоростью {self._speed}')

    def show_speed(self):
        if self._speed > self.speed_limit:
            print('Осторожно! Превышение скоростного режима')
        super().show_speed()


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color=color, name=name, is_police=True)


if __name__ == "__main__":
    tractor = WorkCar('синий', 'Беларус')
    tractor.go()
    tractor.go()
    tractor.turn(Car.DIRECTION_LEFT)
    tractor.go()
    tractor.go()
    tractor.go()
