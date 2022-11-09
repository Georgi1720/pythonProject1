# Задача №1
# Напишите функцию которая пеерворачивает строку 
#def my_function(argument):
#   return argument[::-1]

# Задача №2
# Даны два массива: [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение[1, 2, 2, 3] (порядок не важен)

# array = [1, 2, 3, 2, 0]
# spisok = [5, 1, 2, 7, 3, 2]
# print(list(set(array) & set(spisok)))

# 2 способ
# def intersections(array_1, array_2):
#     array_3 = [i for i in array_1 if i in array_2]
#     return array_3
# print(intersections(array, spisok))


# Задача №3
# Sample Input
#  ["eat", "tea", "tan", "ate", "nat", “bat"]
# Sample Output 
# [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ] 
# Т.е. сгруппировать слова по "общим буквам"

# array = ["eat", "tea", "tan", "ate", "nat", "bat"]
# empty = []
# b = 0
# while b < len(array):
#     for i in range(b ,len(array)):  
#         if sorted(array[b]) == sorted(array[i]) and array[i] not in empty:
#             empty.append(array[i])
#         else:
#             ''
#     b += 1
# print(empty)

#2 способ через словари 
# def group_words(words):
#     result = []
#     words_dict = {}
#     for word in words:
#         sorted_word = "".join(sorted(word))
#         if not sorted_word in words_dict.keys():
#             words_dict[sorted_word] = []
#         words_dict[sorted_word].append(word)
#     for key, value in words_dict.items():
#         result.append(value)
#     return result
# input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
# output = group_words(input_list)
# print(f"input: {input_list}")
# print(f"output: {output}")

