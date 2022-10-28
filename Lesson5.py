#Задача №1
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# text = input('Введите текст: ')
# line = text.split(" ")
# index = 0
# while index < len(line):
#     if line[index].find("а") < 0 and line[index].find("б") < 0 and line[index].find("в") < 0:
#         print(line[index], end=' ')
#         index += 1
#     else:
#         index +=1


# Задача №2 Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#  Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# import random



# player1 = input('Введите имя первого игрока: ')
# player2 = input('Введите имя второго игрока: ')
# print("Идет жеребьевка")
# motion = random.randint(1,2)
# candy = 100
# max_sweets = 28
# if motion == 1: print(f'Игрок {player1} по результатам жерьебьёвки победил и ходит первым')
# else: print(f'Игрок {player2} по результатам жерьебьёвки победил и ходит первым')
# while candy > 0:
#     if motion == 1:
#         print(f'игрок {player1}, Ваш ход! Укажите кол-во забираемых конфет , осталось {candy} шт.')  
#         max_sweets = int(input('(не более 28шт): '))
#         if max_sweets <= 28:
#             candy -= max_sweets
#             motion = 2
#         else:
#             print('Не честно! ')
#             max_sweets = int(input('(не более 28шт): '))
#     if motion == 2:
#         print(f'игрок {player2}, Ваш ход! Укажите кол-во забираемых конфет , осталось {candy} шт.')  
#         max_sweets = int(input('(не более 28шт): '))
#         if max_sweets <= 28:
#             candy -= max_sweets
#             motion = 1
#         else:
#             print('не честно! ')
#             max_sweets = int(input('(не более 28шт): '))   
#     if candy <= 28:
#         if motion == 1:
#             print(f'Осталось {candy} конфет {player1} забирает их, Победа! кариес обеспечен!)')
#             break
#         else:
#             print(f'Осталось {candy} конфет {player2} забирает их, Победа! кариес обеспечен!)')
#             break

# Задча №4
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# with open('text_words.txt', 'w', encoding='UTF-8') as file:
#     file.write(input('Напишите текст необходимый для сжатия: '))
# with open('text_words.txt', 'r') as file:
#     my_txt = file.readline()
#     txt_compr = my_txt.split()

# print(my_txt)

# def file_encod(txt):
#     encond = ''
#     prev_char = ''
#     count = 1
#     if not txt:
#         return ''

#     for char in txt:
#         if char != prev_char:
#             if prev_char:
#                 encond += str(count) + prev_char
#             count = 1
#             prev_char = char
#         else:
#             count += 1
#     else:
#         encond += str(count) + prev_char
#         return encond

# txt_compr = file_encod(my_txt)
# with open('text_code_words.txt', 'w', encoding='UTF-8') as file:
#     file.write(f'{txt_compr}')
# print(txt_compr)
