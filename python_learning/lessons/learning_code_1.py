# Задание 1
# var_1 = 5
# var_2 = 10
# var_3 = "Привет"
# print(var_3)
# print(var_1 + var_2)
# var_1 = input("Введите первое число > ")
# var_2 = input("Введите второе число > ")
# var_3 = input("Введите текст > ")
# print(var_1)
# print(var_2)
# print(var_3)
#
# Задание 2
# time = int(input("Введите время в секундах "))
# hours = time // 3600
# minutes = (time - hours * 3600) // 60
# seconds = time - (hours * 3600 + minutes * 60)
# print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")
#
# Задание 3
# n = input("Введите число: ")
# n_sum = 0
# n_i = ''
# for i in range(3):
#     n_i = n_i + n
#     n_sum = int(n_sum) + int(n_i)
# print(n_sum)
#
# Задание 4
# n = abs(int(input("Введите число ")))
# max = n % 10
# while n >= 1:
#     n = n // 10
#     if n % 10 > max:
#         max = n % 10
#     if n > 9:
#         continue
#     else:
#         print("Самая большая цифра в данном числе - ", max)
#         break
#
# Задание 5
# profit = float(input("Введите выручку фирмы "))
# costs = float(input("Введите издержки фирмы "))
# if profit > costs:
#     print(f"Фирма работает в прибыль, рентабельность выручки - {profit / costs:.2f}")
#     workers = int(input("Введите количество сотрудников фирмы "))
#     print(f"Прибыль в расчёте на одного сотрудника - {profit / workers:.2f}")
# elif profit == costs:
#     print("Фирма работает в ноль")
# else:
#     print("Фирма работает в убыток")
#
# Задание 6
# a = int(input("Результат первой пробежки в КМ "))
# b = int(input("Введите желаемый результат в КМ "))
# result_days = 1
# result_km = a
# while result_km < b:
#     a = a + 0.1 * a
#     result_days += 1
#     result_km = result_km + a
# print(f"Вы достигнете желаемый результат на %.d день" % result_days)
