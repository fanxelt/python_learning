# Задание 1
# present_list = [-55, 55, 55.5, 'Text', None, False]
#
#
# def type_definer(element):
#     for element in range(len(present_list)):
#         print(type(present_list[element]))
#     return
#
#
# type_definer(present_list)

# Задание 2
# element_quantity = int(input("Введите целое значение количества элементов списка -> "))
# present_list = []
# i = 0
# element = 0
# while i < element_quantity:
#     present_list.append(input("Введите следующее значение списка "))
#     i += 1
#
# for elem in range(int(len(present_list) / 2)):
#     present_list[element], present_list[element + 1] = present_list[element + 1], present_list[element]
#     element += 2
# print(present_list)

# Задание 3
# seasons_list = ['winter', 'spring', 'summer', 'autumn']
# month = int(input("Введите порядковый номер месяца -> "))
# if month == 12 or month == 1 or month == 2:
#     print(seasons_list[0])
# elif month == 3 or month == 4 or month == 5:
#     print(seasons_list[1])
# elif month == 6 or month == 7 or month == 8:
#     print(seasons_list[2])
# elif month == 9 or month == 10 or month == 11:
#     print(seasons_list[3])
# else:
#     print("Номер месяца не верный")
#     exit(1)
