# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

SIZE = 98
MIN_ITEM = 1
MAX_ITEM = 10
COLUMNS = 5
ROWS = 4

matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(COLUMNS)] for _ in range(ROWS)]
column = [MAX_ITEM] * len(matrix[0])
max_in_column = MIN_ITEM

for line in matrix:
    for i, item in enumerate(line):
        if item < column[i]:
            column[i] = item
        print(f'{item:>5}', end='')
    print()

for i in column:
    if i > max_in_column:
        max_in_column = i

for item in column:
    print('   --', end='')
print()

for item in column:
    print(f'{item:>5}', end='')
print('\n')

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_in_column}')