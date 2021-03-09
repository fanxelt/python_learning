# Задание 1
# custom_list = []
# while True:
#     line = input("Ввод: ")
#     if line == '':
#         print(custom_list)
#         exit()
#     else:
#         newline = line + '\n'
#         custom_list.append(newline)
#
#     with open("list_1.txt", "w") as file_obj:
#         file_obj.writelines(custom_list)

# Задание 2
# with open("list_2.txt") as file_obj:
#     lines = 0
#     letters = 0
#     for line in file_obj:
#         lines += line.count("\n")
#         letters = len(line)-1
#         print(f"{letters} букв в слове.")
#     print(f"Текст насчитывает {lines} линий")

# Задание 3
# with open("list_3.txt", "r") as file_obj:
#     money_sum = 0
#     count = 0
#     people = []
#     for line in file_obj:
#         print(line, end='')
#         tokens = line.split(':')
#         if float(tokens[1]) <= 20000.0:
#             people.append(tokens[0])
#         money_sum += float(tokens[1])
#         count += 1
# average_sum = money_sum / count
# print(f"Люди имеющие низкий оклад: {people}")
# print(f"Средний доход: {average_sum}")

# Задание 4
# translator = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
# custom_list = []
# result = []
# try:
#     file_obj = open('list_4.txt', 'r')
#     for line in file_obj:
#         tokens = line.split(' - ')
#         print(tokens)
#         if tokens[0] in translator:
#             word = translator[tokens[0]]
#             result.append(word + ' - ' + tokens[1])
#     print(result)
# except IOError:
#     print('Произошла ошибка ввода-вывода!')
# finally:
#     file_obj.close()
#
# try:
#     file_input = open('list_4_translated.txt', 'w')
#     file_input.writelines(result)
# except IOError:
#     print('Произошла ошибка ввода-вывода!')
# finally:
#     file_input.close()

# Задание 5
# def summary():
#     try:
#         with open('list_5.txt', 'w+') as file_obj:
#             line = input('Введите цифры через пробел \n')
#             file_obj.writelines(line)
#             present_number = line.split()
#
#             print(sum(map(int, present_number)))
#     except IOError:
#         print('Произошла ошибка ввода-вывода!')
#     except ValueError:
#         print('Неправильный ввод!')
# summary()

# Задание 6
# subj = {}
# with open('list_6.txt', 'r') as init_f:
#     for line in init_f:
#         subject, lecture, practice, lab = line.split()
#         subj[subject] = int(lecture) + int(practice) + int(lab)
#     print(f'Общее количество часов по предмету - \n {subj}')

# Задание 7
import json
profit = {}
result = {}
profitable = 0
profit_average = 0
i = 0
with open('list_7.txt', 'r') as file:
    for line in file:
        name, firm_type, earning, cost = line.split()
        profit[name] = int(earning) - int(cost)
        if profit.setdefault(name) >= 0:
            profitable = profitable + profit.setdefault(name)
            i += 1
    if i != 0:
        profit_average = profitable / i
        print(f'Прибыль средняя - {profit_average:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    result = {'средняя прибыль': round(profit_average)}
    profit.update(result)
    print(f'Прибыль каждой компании - {profit}')

with open('list_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')
