# Задача №1
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# number = input("Ввдеите число: ")
# result = 0
# index = 0
# while index < len(number):
#     if number[index] != '.':
#         result += int(number[index])
#         index += 1
#     else:
#         index += 1
# print(result)

# Задача №2
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# number = int(input("Введите число: "))
# meaning = 1
# for i in range(1, number+1):
#     meaning *= i
#     print(meaning, end=' ')

# Задача №3
# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# a = int(input("Введите число: "))
# index = 1
# summ = 0
# while index <= a:
#     meaning = round((1+1/index)**index, 2)
#     print(index, ":", meaning, end=' | ')
#     index += 1
#     summ += meaning
# print('\n', summ)

# Задача №4  третий семинар не просмотрен , задачу пока не сдалал
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
# some_list = [-5, 4, 3, 2, 5]
# data = open('123.txt', 'w')
# data.close()


# Задача № 5
# # Реализуйте алгоритм перемешивания списка.
# import random
# some_list = [0, 1, 2, 3, 5, 6, ]
# random.shuffle(some_list)
# print(some_list)

# ДОП. задача на алгоритмы с реальных собеседований
# Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение
# [1, 2, 2, 3]
# some_list1 = [1, 2, 3, 2, 0]
# some_list2 = [5, 1, 2, 7, 3, 2]
# empty_array = []
# for i in some_list1:
#     for k in some_list2:
#         if i == k:
#             empty_array.append(i)
#             break
#
# print(empty_array)







