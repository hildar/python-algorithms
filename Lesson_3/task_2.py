# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо
# заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
array2 = []

print(array1)

for i, item in enumerate(array1):
    if item % 2 == 0:
        array2.append(i)

print(array2)
