# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Попробуйте использовать метод count(), а также решите задачу с помощью своего алгоритма (без count).
# Замерьте время работы двух алгоритмов и сравните, подумайте, почему оно отличается.
#     колво элементов в массиве = 5
#     массив = 1 2 3 4 5
#     нужно найти число = 3
#     число 3 встречается -> 1 раз

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


