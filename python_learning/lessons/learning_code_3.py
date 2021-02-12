# Задание 1
# def divide_func(x, y):
#     try:
#         a = x / y
#         return a
#     except ZeroDivisionError:
#         return "Ошибка, деление на ноль запрещено."
#     except ValueError:
#         return "Ошибка ввода, необходимо вводить число."
#
#
# print(divide_func(int(input("Введите первое число -> ")), int(input("Введите второе число -> "))))

# Задание 2
# def human_data(name, surname, birth_year, city, email, phone):
#     print(name, surname, birth_year, city, email, phone)
#
#
# human_data(name=input("Введите имя -> "),
#            surname=input("Введите фамилию -> "),
#            birth_year=input("Введите год рождения -> "),
#            city=input("Введите город проживания -> "),
#            email=input("Введите электронную почту -> "),
#            phone=input("Введите номер телефона -> "))

# Задание 3
# def count_func(x, y, z):
#     sequence = [x, y, z]
#     total = []
#     max_1 = max(sequence)
#     total.append(max_1)
#     sequence.remove(max_1)
#     max_2 = max(sequence)
#     total.append(max_2)
#     print(sum(total))
#
#
# count_func(int(input("Введите первое число -> ")),
#            int(input("Введите второе число -> ")),
#            int(input("Введите третье число -> ")))

# Задание 4
# def my_func(x, y):
#     if y == 0:
#         return 1.0
#     if y < 0:
#         y *= -1
#     x_start = x
#     for i in range(1, y):
#         x *= x_start
#
#     return 1.0 / x
#
#
# print(my_func(int(input("Введите положительное число -> ")),
#               int(input("Введите отрицательное число -> "))))

# Задание 5
# def summary_func():
#     sum_res = 0
#     execution = True
#     while execution is True:
#         number = input("Введите число или Q для выхода -> ").split()
#
#         res = 0
#         for element in range(len(number)):
#             if number[element] == "q" or number[element] == "Q":
#                 execution = False
#                 break
#             else:
#                 res = res + int(number[element])
#         sum_res = sum_res + res
#         print(f"Текущая сумма -> {sum_res}")
#     print(f"Окончательная сумма -> {sum_res}")
#
#
# summary_func()

# Задание 6
# def int_func():
#     word = input("Введите слова -> ")
#     print(word.title())
#     return
#
#
# int_func()
