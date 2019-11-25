# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title=None):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        if self.title == 'да':
            print('Рисуем ручкой!')
        else:
            print('Есть и другие варианты!')


class Pencil(Stationery):
    def draw(self):
        if self.title == 'да':
            print('Рисуем карандашом!')
        else:
            print('А если?')


class Handle(Stationery):
    def draw(self):
        if self.title == 'да':
            print('Рисуем маркером!')
        else:
            print('Может ты и не хотел рисовать?!')


title = input('Как будет называться Ваш проект? ')
print(f'\nНазвание проекта - {title}')
art_art = Stationery()
art_art.draw()

first_art = Pen(input('Чем будете рисовать, Ручка? \n'))
first_art.draw()

second_art = Pencil(input('Карандаш? \n'))
second_art.draw()

third_art = Handle(input('Маркер? \n'))
third_art.draw()
