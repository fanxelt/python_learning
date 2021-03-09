# Task 1
# from time import sleep
#
#
# class TrafficLight:
#     __color = ['Red', 'Yellow', 'Green']
#
#     def running(self):
#         i = 0
#         while i < 3:
#             print(f'Color swaps \n '
#                   f'{TrafficLight.__color[i]}')
#             if i == 0:
#                 sleep(7)
#             elif i == 1:
#                 sleep(2)
#             elif i == 2:
#                 sleep(5)
#             i += 1
#
#
# TrafficLight = TrafficLight()
# TrafficLight.running()

# Task 2
# class Road:
#     def __init__(self, length, width, mass=2.5, thickness=0.05):
#         self._length = length
#         self._width = width
#         self._mass = mass
#         self._thickness = thickness
#
#     def need(self):
#         need = self._length * self._width * self._mass * self._thickness
#         print(f'The need for {need} tons of cement')
#
#
# Road_1 = Road(20, 5000)
# Road_1.need()

# Task 3
# class Worker:
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": wage, "bonus": bonus}
#
#
# class Position(Worker):
#
#     def __init__(self, name, surname, position, wage, bonus):
#         super().__init__(name, surname, position, wage, bonus)
#
#     def get_full_name(self):
#         print(self.name + ' ' + self.surname)
#
#     def get_position(self):
#         print(self.position)
#
#     def get_total_income(self):
#         print(self._income.get('wage') + self._income.get('bonus'))
#
#
# john = Position('John', 'Doe', 'Programmer', 90000.0, 13990.0)
# john.get_full_name()
# john.get_position()
# john.get_total_income()

# Task 4
# class Car:
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self):
#         return f'{self.name} is started'
#
#     def stop(self):
#         return f'{self.name} is stopped'
#
#     def turn_right(self):
#         return f'{self.name} is turned right'
#
#     def turn_left(self):
#         return f'{self.name} is turned left'
#
#     def show_speed(self):
#         return f'Current speed of {self.name} is {self.speed}'
#
#     def police(self):
#         if self.is_police:
#             return f'The {self.name} car is from police department'
#         else:
#             return f'The {self.name} car is not from police department'
#
#
# class TownCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#     def show_speed(self):
#         print(f'Current speed of town car {self.name} is {self.speed}')
#
#         if self.speed >= 41:
#             return f'The speed of {self.name} is higher than allow for town car'
#         else:
#             return f'The speed of {self.name} is normal for town car'
#
#
# class SportCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#
# class WorkCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#     def show_speed(self):
#         print(f'Current speed of work car {self.name} is {self.speed}')
#
#         if self.speed >= 61:
#             return f'The speed of {self.name} is higher than allow for work car'
#
#
# class PoliceCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#
# toyota = TownCar(100, 'Blue', 'Toyota', False)
# nissan = SportCar(80, 'Red', 'Nissan', False)
# lada = WorkCar(60, 'Black', 'Lada', False)
# niva = PoliceCar(9001, 'Blue', 'Niva', True)
# print(lada.go())
# print(lada.turn_left())
# print(lada.turn_right())
# print(f'{lada.name} is {lada.color}')
# print(f'Is {lada.name} a police car? {lada.is_police}')
# print(f'Is {toyota.name} a police car? {toyota.is_police}')
# print(toyota.show_speed())
# print(nissan.show_speed())
# print(niva.police())
# print(niva.show_speed())

# Task 5
# Actually the task 5 is shown in any upper task. No need for repeat.

# Task 6
# class Stationary:
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         return f'Draw start {self.title}'
#
#
# class Pen(Stationary):
#     def __init__(self, title):
#         super().__init__(title)
#
#     def draw(self):
#         return f'You picked up {self.title}. Starting {self.title} draw...'
#
#
# class Pencil(Stationary):
#     def __init__(self, title):
#         super().__init__(title)
#
#     def draw(self):
#         return f'You picked up {self.title}. Starting {self.title} draw...'
#
#
# class Marker(Stationary):
#     def __init__(self, title):
#         super().__init__(title)
#
#     def draw(self):
#         return f'You picked up {self.title}. Starting {self.title} draw...'
#
#
# pen = Pen('pen')
# pencil = Pencil('pencil')
# marker = Marker('marker')
# print(pen.draw())
# print(pencil.draw())
# print(marker.draw())
