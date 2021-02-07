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
# seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
#
# month = int(input("Введите порядковый номер месяца -> "))
# if month == 12 or month == 1 or month == 2:
#     print(seasons_list[0])
#     print(seasons_dict.get(1))
# elif month == 3 or month == 4 or month == 5:
#     print(seasons_list[1])
#     print(seasons_dict.get(2))
# elif month == 6 or month == 7 or month == 8:
#     print(seasons_list[2])
#     print(seasons_dict.get(3))
# elif month == 9 or month == 10 or month == 11:
#     print(seasons_list[3])
#     print(seasons_dict.get(4))
# else:
#     print("Номер месяца не верный")
#     exit(1)

# Задание 4
# present_string = input("Введите текст -> ")
# present_words = []
# count = 1
# for i in range(present_string.count(' ') + 1):
#     present_words = present_string.split()
#     if len(str(present_words)) <= 10:
#         print(f"{count}.{present_words[i]}")
#         count += 1
#     else:
#         print(f"{count}.{present_words[i][0:10]}")
#         count += 1

# Задание 5
# rating_list = [3, 2, 1]
# print("Рейтинг -", rating_list)
# number = int(input("Введите число в рейтинговый лист -> "))
# c = rating_list.count(number)
# for element in rating_list:
#     if c > 0:
#         i = rating_list.index(number)
#         rating_list.insert(i + c, number)
#         break
#     else:
#         if number > element:
#             j = rating_list.index(element)
#             rating_list.insert(j, number)
#             break
#         elif number < rating_list[len(rating_list) - 1]:
#             rating_list.append(number)
# print("Новый рейтинг -", rating_list)

# Задание 6 TBD/Optional
