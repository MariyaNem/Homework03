# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Попробуйте использовать метод count(), а также решите задачу с помощью своего алгоритма (без count).
# Замерьте время работы двух алгоритмов и сравните, подумайте, почему оно отличается.

# import time
# array_a = []
# list_len = int(input("Введите количество элементов в массиве: "))
# for _ in range(list_len):
#     array_a.append(int(input("Введите число: ")))

# count = 0
# found_num = int(input('Число для подсчёта в массиве: '))
# start = time.perf_counter()
# for i in range(list_len):
#     if array_a[i] == found_num:
#         count += 1
# print('Число', found_num,'встречается в массиве', count, 'раз')
# end = time.perf_counter()
# print(end-start)

# # Способ с count()
# found_num = int(input('Число для подсчёта в массиве: '))
# start = time.perf_counter()
# num = array_a.count(found_num)
# print('Число', found_num,'встречается в массиве', num, 'раз')
# end = time.perf_counter()
# print(end-start)


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  
# строках записаны N целых чисел Ai. Последняя строка содержит число X
#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих
#строках записаны N целых чисел Ai. Последняя строка содержит число X

# import sys

# input_list = []
# list_len = int(input("Введите количество элементов массива: "))
# for _ in range(list_len):
#     input_list.append(int(input("Введите число: ")))
# print(input_list)

# found_num = int(input('Заданное число: '))
# near_num = 0

# for i in range(list_len):
#     if input_list[i] == found_num:
#         print('Искомое число присутствует в массиве: ', input_list[i])
#         sys.exit()
#     elif i == 0:
#         if found_num > input_list[i]:
#             min_diff = found_num - input_list[i]
#         else:
#             min_diff = input_list[i] - found_num
#     else:
#         if input_list[i] > found_num:
#             diff = input_list[i] - found_num
#             if min_diff > diff:
#                 min_diff = diff
#                 near_num = input_list[i]
#         else:
#             diff = found_num - input_list[i]
#             if min_diff > diff:
#                 min_diff = diff
#                 near_num = input_list[i]
# print('Ближайшее число: ', near_num)


# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так: A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка;
# B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка
# Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход
# подается только одно слово, которое содержит либо только английские, либо только русские буквы.
#
# ноутбук -> 12

# summ = 0
# dictionary = {1: 'aeioulnstrавеинорст', 2: 'dgдклмпу', 3: 'bcmpбгёья', 4: 'fhvwyйы', 5: 'kжзхцч', 8: 'jxшэю', 10: 'qzфщъ'}
# word = str(input('Введите слово на английском или русском: '))

# for i in range(len(word)):
#     for key, value in dictionary.items():
#         if word[i] in value:
#             summ += key
# print(summ)