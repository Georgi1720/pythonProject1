# Задача 1, 2: Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
# num_translate_adv("One")
# "Один"
# num_translate_adv("two")
# "два"

# def num_translate_adv(line):
#     my_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
#                'seven': 'семь',
#                'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
#
#     if my_dict.get(line) != None : return print(my_dict.get(line))
#     elif my_dict.get(line) == None:
#         if line.lower() in my_dict:
#             x = line.lower()
#             return print(my_dict.get(x).title())
#         else: print(my_dict.get(line))
#
# num_translate_adv('ten')


# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
# thesaurus("Иван", "Мария", "Петр", "Илья")
# {
# "И": ["Иван", "Илья"],
# "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам? Можно ли использовать словарь в этом случае?

# def thesaurus(some_list):
#     from collections import defaultdict
#     alphabet = [chr(i) for i in range(ord('А'), ord('Я') + 1)]
#     empty_dict = defaultdict(list)
#     i = 0
#     j = 0
#     while i < len(some_list):
#         while j < len(alphabet):
#             if some_list[i][:1] == alphabet[j]:
#                 empty_dict[alphabet[j]].append(some_list[i])
#             else:
#                 pass
#             j += 1
#         i += 1
#         j = 0
#     return empty_dict
#
#
# name_list = ["Андраник", "Иван", "Мария", "Петр", "Илья", "Ильяс", "Гарик", "Гоша"]
# print(thesaurus(name_list))


