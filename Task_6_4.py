# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
import random


class Car:
    def __init__(self, speed=0, color=None, name=None, **kwargs):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
        self.direction = None

    def show_speed(self):
        (print(f'Текущая скорость {self.speed} км/ч'))

    def go_car(self):
        if self.speed > 0:
            print('Машина двигается!')

    def stop_car(self):
        if self.speed == 0:
            print('Машина остановилась!')

    def turn_car(self):
        if self.direction == 'лево':
            print('Вы повернули на лево!')
        elif self.direction == 'право':
            print('Вы повернули на право!')
        else:
            print('Вы продолжаете движение прямо!')


class TownCar(Car):
    def __init__(self, speed, color, name, direction='право'):
        super().__init__(speed, color, name)
        self.direction = direction

    def show_speed(self):
        if self.speed > 60:
            print(f'Вы превысили, Ваша скорость {self.speed} км/ч!'
                  f' На этом виде транспорта скорость не может быть выше 60 км/ч')
        elif self.speed == 0:
            self.stop_car()
        else:
            print('Хорошей дороги!')


class SportCar(Car):
    def __init__(self, speed=150, color='КРАСНЫЙ', name='Ferrari'):
        super().__init__(speed, color, name)
        self.speed = speed
        self.color = color
        self.name = name


class WorkCar(Car):
    def show_speed(self,):
        if self.speed > 40:
            print('Вы превышаете, на этом виде транспорта скорость не может быть выше 40 км/ч')
        elif self.speed == 0:
            self.stop_car()
        else:
            print(f'Вы двигаетесь со скоростью {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True
        self.direction = 'лево'


# car_1 = TownCar(random.randint(0, 80), input('выберите цвет авто: '),
#                 input('введите марку автомобиля: '))
# car_1.go_car()
# car_1.turn_car()
# car_1.stop_car()
# print(f'Ваша скорость: {car_1.speed}')
# print(f'Вы за рулем {car_1.color}', f'{car_1.name}')
# car_1.show_speed()
# print(f'Это полицейский автомобиль: {car_1.is_police}\n')
#
# car_2 = WorkCar(random.randint(0, 60), 'красный', 'gaz')
# car_2.go_car()
# car_2.turn_car()
# car_2.stop_car()
# print(f'Ваша скорость: {car_2.speed}')
# print(f'Вы за рулем {car_2.color}', f'{car_2.name}')
# car_2.show_speed()
# print(f'Это полицейский автомобиль: {car_2.is_police}\n')
#
# car_3 = SportCar(random.randint(0, 200))
# car_3.go_car()
# car_3.turn_car()
# car_3.stop_car()
# print(f'Ваша скорость: {car_3.speed}')
# print(f'Вы за рулем {car_3.color}', f'{car_3.name}')
# car_3.show_speed()
# print(f'Это полицейский автомобиль: {car_3.is_police}\n')

car_4 = PoliceCar(random.randint(0, 200), 'бело-черный', 'Lamborgini')

print(f'Ваша скорость: {car_4.speed}')
print(f'Вы за рулем {car_4.color}', f'{car_4.name}')
car_4.go_car()
car_4.turn_car()
car_4.stop_car()
car_4.show_speed()
print(f'Это полицейский автомобиль: {car_4.is_police}')


