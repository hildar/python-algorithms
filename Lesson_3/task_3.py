# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
min_num = array[0]
max_num = array[SIZE - 1]
min_index, max_index = 0, 0
print(array)

for i, item in enumerate(array):
    if item < min_num:
        min_num = item
        min_index = i
    if item >= max_num:
        max_num = item
        max_index = i

array[min_index], array[max_index] = array[max_index], array[min_index]
print(array)