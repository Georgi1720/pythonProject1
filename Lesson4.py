# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# number = float(input('Введите число: '))
# accuracy = int(input('Введите точность: '))
# print(str(round(number, accuracy+1))[:-1])

#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# number = int(input('Введите число: '))
# empty = []
# index = 2
# while number != 1:
#     if number % index == 0:
#         empty.append(index)
#         number /= index
#     else:
#         index += 1
# print(empty)

# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
# some_list = [2, 2, 2 ,3, 3, 4, 4, 4, 5]
# b = []
# for i in some_list:
#     if some_list.count(i) == 1:
#         b.append(i)
# print(b)


# print(set(some_list))
