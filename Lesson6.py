# Дан список: ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
# (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
# Главное: дополнить числа до двух разрядов нулём!

# line = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# line_1 = []
# line_2 = []
# i = 0
# while i < len(line):
#     if line[i].isalpha() == False:
#         line_1.append('"')
#         if len(line[i]) == 1:
#             line_1.append('0' + line[i])
#             line_1.append('"')
#             i += 1
#         elif len(line[i]) == 2:
#             Decompose = list(line[i])
#             if Decompose[0] == '+' or Decompose[0] == '-':
#                 Decompose.insert(1, '0')
#                 a = ''.join(Decompose)
#                 line_1.append(a)
#                 line_1.append('"')
#                 i += 1
#             else:
#                 a = ''.join(Decompose)
#                 line_1.append(a)
#                 line_1.append('"')
#                 i += 1
#     else:
#         line_1.append(line[i])
#         i += 1
#
#
# k = 0
# while k < len(line_1):
#     if line_1[k] == '"':
#         k += 1
#     elif line_1[k].isalpha() == False:
#         add = list('"' + line_1[k] + '"')
#         a = ''.join(add)
#         line_2.append(a)
#         k += 1
#     else:
#         line_2.append(line_1[k])
#         k += 1
#
# result = ' '.join(line_2)
#
#
# print(f'Оригинал  => {line}')
# print(f'Список c кавычками => {line_1}')
# print(f'Итоговый список =>  {result}')


# 4. Дан список, содержащий искажённые данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида: 'Привет, Игорь!'
#  Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.
#   Можно ли при этом не создавать новый список?

# some_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
#
#
# def roll_call(line):
#     split_line = line.split(' ')
#     name = split_line[-1]
#     return name.title()
#
# for i in some_list:
#     print(f'Привет, {roll_call(i)}!')

# 5. Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек
# (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

import random as r

some_list = [57.8, 46.51, 97, 35.4, 84.11, 89.1, 55.55, 74.3, 55, 59.99]
# empty = [round(r.uniform(1.1, 99.99), 2) for i in range(10)]

def monetary_format(list_meaning):
    list_meaning.sort()
    i = 0
    rub = 'руб'
    kop = 'коп'
    while i < len(list_meaning):
        if type(list_meaning[i]) == float:
            split_line = str(list_meaning[i]).split('.')
            left = split_line[0]
            if len(split_line[1]) == 1:
                right = '0' + str(split_line[1])
            else:
                right = split_line[1]
            i += 1
        else:
            left = list_meaning[i]
            right = '00'
            i += 1
        print(f'{left}{rub} {right}{kop}', end=', ')


def revers_monetary_format(list_meaning):
    list_meaning = sorted(list_meaning, reverse=True)
    i = 0
    rub = 'руб'
    kop = 'коп'
    while i < len(list_meaning):
        if type(list_meaning[i]) == float:
            split_line = str(list_meaning[i]).split('.')
            left = split_line[0]
            if len(split_line[1]) == 1:
                right = '0' + str(split_line[1])
                i += 1
            else:
                right = split_line[1]
                i += 1

        else:
            left = list_meaning[i]
            right = '00'
            i += 1
        print(f'{left}{rub} {right}{kop}', end=', ')



print(f'Изначальный список => {some_list}')
monetary_format(some_list)
print()
revers_monetary_format(some_list)
print()
revers_monetary_format(some_list[:5])





