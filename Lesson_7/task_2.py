# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


# merge
def merge(left, right):
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


# merge sort
def merge_sort(array):
    # base case
    if len(array) <= 1:
        return array

    # initialization
    left, right, result = [], [], []
    pivot = len(array) // 2

    # filling arrays
    for i in range(pivot):
        left.append(array[i])
    for i in range(pivot, len(array)):
        right.append(array[i])

    # recursion call and merge
    return merge(merge_sort(left), merge_sort(right))


# Не уверен что я правильно понял какой должен быть массив, поэтому написал два варианта, выберете правильный)
array = [float(i) for i in range(50)]
# array = [random.uniform(0, 49.999999) for i in range(10)]

random.shuffle(array)
print(array)

array = merge_sort(array)
print(array)
