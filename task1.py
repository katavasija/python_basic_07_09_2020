"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
и метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import signal
import sys
import time


class TrafficLight:
    COLOR_RED = 'RED'
    COLOR_GREEN = 'GREEN'
    COLOR_YELLOW = 'YELLOW'

    def __init__(self, color):
        self.__color = ''
        self.__code_red = True
        self.__color_pauses = {TrafficLight.COLOR_RED: 7, TrafficLight.COLOR_YELLOW: 2, TrafficLight.COLOR_GREEN: 10}
        self.__color_messages = {TrafficLight.COLOR_RED: "Красный. Стоп!",
                                 TrafficLight.COLOR_YELLOW: "Желтый. Готовьтесь!",
                                 TrafficLight.COLOR_GREEN: "Зеленый. Можно!"}
        self.set_color(color)

    def set_color(self, color):
        assert color in (TrafficLight.COLOR_RED, TrafficLight.COLOR_YELLOW, TrafficLight.COLOR_GREEN), \
            f"Неверно задан цвет сигнала:{color}"
        self.__color = color
        if self.__color == TrafficLight.COLOR_GREEN:
            self.__code_red = False
        elif self.__color == TrafficLight.COLOR_RED:
            self.__code_red = True

    def get_color(self):
        return self.__color

    def get_message(self):
        return self.__color_messages[self.__color]

    def get_pause_seconds(self):
        return self.__color_pauses[self.__color]

    def running(self):
        while True:
            print(self.get_message())
            time.sleep(self.get_pause_seconds())
            self.__change_color()


    def __change_color(self):
        if self.__color in (TrafficLight.COLOR_RED, TrafficLight.COLOR_GREEN):
            self.set_color(TrafficLight.COLOR_YELLOW)
        elif self.__color == TrafficLight.COLOR_YELLOW:
            if self.__code_red:
                self.set_color(TrafficLight.COLOR_GREEN)
            else:
                self.set_color(TrafficLight.COLOR_RED)


def ctrlc_handler(*args):
    print('Работа сфетофора прекращена!')
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, ctrlc_handler)
    traf_light = TrafficLight(TrafficLight.COLOR_RED)
    traf_light.running()
    signal.pause()
