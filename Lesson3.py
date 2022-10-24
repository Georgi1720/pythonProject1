 # Задача №1
 # Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
 # Пример:
 # [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# some_list = [12, 1, 3, 35, 45, 5]
# summ = 0
# index = 1
# while index < len(some_list):
#     summ += some_list[index]
#     index += 2
# print(summ)

# Задача №2
#  Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#  Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


# some_list = [2, 3, 4, 5, 6]
# epmty_list = []
# index_left = 0
# index_right = -1
# while index_left < len(some_list)/2:
#     temp = some_list[index_left] * some_list[index_right]
#     index_left += 1
#     index_right -=1
#     epmty_list.append(temp)
#     temp = 0
# print(epmty_list)

# Задача №3
# Задайте список из вещественных чисел. Напишите программу,
#  которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# some_list = [1.1, 1.2, 3.1, 5, 10.01]
# empty_list = []
# index = 0
# for index in range(len(some_list)):
#     temp = some_list[index]%1
#     empty_list.append(temp)
#     temp = 0
# result = max(empty_list)-min(empty_list)
# print(result)

# Задача №4
#  Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#  Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# a = int(input("Введите число: "))
# print(format(a, 'b'))
