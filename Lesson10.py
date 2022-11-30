# -----------------------------------------------Задача №1 ----------------------------------------------------
# Реализуйте классы MinStat, MaxStat, AverageStat, которые будут находить минимум, максимум и среднее арифметическое последовательности целых чисел.
# Экземпляры классов инициализируются без аргументов. Метод add_number должен добавлять в статистику число,
#  которое будет учтено при вычислении финального результата методом result.
# Для экземпляров MinStat и MaxStat result должен возвращать целое число, для AverageStat — число типа float 
# (это число будет сравниваться с правильным ответом до седьмой значащей цифры).
# Если в последовательности отсутствуют числа и статистические величины вычислить невозможно, метод result должен возвращать None.

# values = [10, 2, 4, 5, 8, 45, 1]
# class MinStat:   
#     def __init__(self):
#         self.some_list = []
    
#     def add_number(self,number):
#         x = self.some_list.append(number)

#     def result(self):
#        return min(self.some_list)

# class MaxStat:   
#     def __init__(self):
#         self.some_list = []
    
#     def add_number(self,number):
#         x = self.some_list.append(number)

#     def result(self):
#        return max(self.some_list)

# class AverageStat:   
#     def __init__(self):
#         self.some_list = []
    
#     def add_number(self,number):
#         x = self.some_list.append(number)

#     def result(self):
#         x = str(round(sum(self.some_list)/len(self.some_list),3))[:-1]
#         return x


# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()
# for v in values:
#     mins.add_number(v)
#     maxs.add_number(v)
#     average.add_number(v)

# print(mins.result(),maxs.result(), average.result())

#--------------------------------------------------Задача №2---------------------------------------------------------

# Реализуйте класс Table, который хранит целые числа в двумерной таблице.
#  При инициализации Table(rows, cols) экземпляру передаются число строк и столбцов в таблице.
#  Строки и столбцы нумеруются с нуля.


# class Table:

#     def __init__(self,row, col):
#         self.row = row
#         self.col = col
#         self.table = [[0] * col for i in range(row)]

#     def get_value(self, row, col):
#         if row < self.row and col < self.col: return self.table[row][col]
#         else: return None

#     def set_value(self, row, col, value):
#         self.table[row][col] = value

#     def n_rows(self):
#         return self.row

#     def n_cols(self):
#         return self.col

#     def delete_row(self,row):
#         self.table.pop(row)
#         self.row -= 1

#     def delete_col(self,col):
#         for row in range(self.row):
#             self.table[row].pop(col)
#         self.col -= 1

#     def add_row(self,row):
#         self.table.insert(row, [0]* self.col)
#         self.row +=1


#     def add_col(self,col):
#         for row in range(self.row):
#             self.table[row].insert(col,0)
#         self.col += 1





# tab = Table(1, 1)

# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()

# tab.set_value(0, 0, 1000)

# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()

# for i in range(-1, tab.n_rows() + 1):
#     for j in range(-1, tab.n_cols() + 1):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()

# tab.add_row(0)
# tab.add_row(2)
# tab.add_col(0)
# tab.add_col(2)

# tab.set_value(0, 0, 2000)
# tab.set_value(0, 2, 3000)
# tab.set_value(2, 0, 4000)
# tab.set_value(2, 2, 5000)

# for i in range(-1, tab.n_rows() + 1):
#     for j in range(-1, tab.n_cols() + 1):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()
