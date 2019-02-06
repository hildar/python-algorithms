# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

SIZE = 10000
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
    print(f'Массив array не имеет отрицательных элементов')



import sys

# ******************************** Home work **********************************
#
#
# Функция для проверки памяти
def show_sizeof(x, summ=0):
    # Если является строкой, то сразу возвращаем сумму + размер
    if isinstance(x, str):
        return summ + sys.getsizeof(x)

    # Проверяем что объект итерируется (списки, кортежи, множества и т.д.)
    elif hasattr(x, '__iter__'):
        summ += sys.getsizeof(x)
        # проверка на словарь dict{}
        if hasattr(x, 'items'):
            for item in x.items():
                if hasattr(item, '__iter__'):
                    # повторный вызов функции если объект итерируемый
                    summ = show_sizeof(item, summ)
                else:
                    summ += sys.getsizeof(item)
        else:
            for item in x:
                if hasattr(item, '__iter__'):
                    # повторный вызов функции если объект итерируемый
                    summ = show_sizeof(item, summ)
                else:
                    summ += sys.getsizeof(item)
        return summ
    # иначе int, float etc.
    else:
        return sys.getsizeof(x)


# При увеличении SIZE увеличивается объем потребляемой памяти
array_var = [MIN_ITEM, MAX_ITEM, SIZE, max_num, idx, array]
print(f'total memory = {show_sizeof(array_var)} byte')
# Python 3.7.2, Разрядность - x64
