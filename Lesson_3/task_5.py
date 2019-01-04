# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

SIZE = 10
MIN_ITEM = -5
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

max_num = MIN_ITEM
idx = 0

for i, item in enumerate(array):
    if max_num < item < 0:
        max_num = item
        idx = i

print(f'Массив array: {array}')
if idx > 0:
    print(f'Максимальный отрицательный элемент в массиве array: {max_num}\n'
          f'находящийся на позиции: {idx}')
else:
    print(f'Массив array не имеет отрицптельных элементов')
