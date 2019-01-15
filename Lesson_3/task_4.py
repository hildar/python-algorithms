# 4. Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 20
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
array2 = [0 for _ in range(MIN_ITEM, MAX_ITEM + 1)]  # создаем для использования индексов

for i in array:
    array2[i - MIN_ITEM] += 1

max_num = 0
spam_max = 0

for i, item in enumerate(array2):
    if item > spam_max:
        spam_max = item
        max_num = i

print(f'Массив array: {array}')
print(f'Чаще всего в массиве array встречается число: {max_num + MIN_ITEM}')
