# Задание 1
# from sys import argv
#
# name, workout_time, salary, award = argv
#
# calc = (int(workout_time) * int(salary)) + int(award)
#
# print(f"Ваша зарплата равна {calc}.")

# Задание 2
# present_list = [2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# calculations = [el for el in present_list if el > present_list[present_list.index(el) - 1]]
# print(calculations)

# Задание 3
# numbers = range(20, 241)
# calculations = [el for el in numbers if el % 20 == 0 or el % 21 == 0]
# print(calculations)

# Задание 4
# present_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# calculations = [el for el in present_list if present_list.count(el) == 1]
# print(calculations)

# Задание 5
# from functools import reduce
#
#
# def calculations_func(calc_el, el):
#     return calc_el * el
#
#
# print(f'Список четных значений {[el for el in range(99, 1001) if el % 2 == 0]}')
# print(f'Результат перемножения всех элементов списка {reduce(calculations_func, [el for el in range(99, 1001) if el % 2 == 0])}')

# Задание 6
# from itertools import count
#
# for el in count(int(input('Введите стартовое число -> '))):
#     print(el)

# from itertools import cycle
#
# present_list = ["A", True, False, 1, 2, None]
# for el in cycle(present_list):
#     print(el)

# Задание 7
# from itertools import count
# from math import factorial
#
#
# def generator():
#     for el in count(1):
#         yield factorial(el)
#
#
# gen = generator()
# x = 0
# for i in gen:
#     if x < 15:
#         print(i)
#         x += 1
#     else:
#         break
