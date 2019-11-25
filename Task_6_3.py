# Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name=None, surname=None, position=None, **kwargs):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": 0, "bonus": 0}
        # self.full_name = None

    # def get_full_name(self):
    #     print(f'{self.full_name}')


class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)
        self._income = {"wage": 200, "bonus": 70}

    def get_full_name(self,):
        return print(f'Уважаемый {self.name} {self.surname}, ')

    def get_total_income(self):
        pass

# worker_1 = Worker('Иван', 'Иванов', 'токарь')
# worker_1.get_full_name()

worker_2 = Position('Ivan', 'Ivanov', 'killer')
worker_2.get_full_name()
# worker_2.get_total_income()
