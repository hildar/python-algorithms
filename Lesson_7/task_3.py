# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

import random


def partition(array, first, last):

    pivot = array[last]
    i = first - 1

    for j in range(first, last):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[last] = array[last], array[i + 1]

    # q = random.randint(first, last)
    # pivot = array[q]
    # i, j = first, last
    #
    # while i <= j:
    #     while array[i] < pivot:
    #         i += 1
    #     while array[j] > pivot:
    #         j -= 1
    #
    #     if i <= j:
    #         array[i], array[j] = array[j], array[i]
    #         i += 1
    #         j -= 1

    return i + 1


def select(array, first, last, i):
    # base case
    if first >= last:
        return array[first]

    q = partition(array, first, last)
    k = q - first + 1   # Плюс один опорный элемент

    if i == k:
        return array[q]  # Ответом является опорное значение
    elif i < k:

        return select(array, first, q - 1, i)
    else:
        return select(array, q + 1, last, i - k)


m = 4

# array = [random.randrange(0, 100) for i in range(2 * m + 1)]
array = [i * i * 2 for i in range(2 * m + 1)]
# array = [2, 8, 7, 1, 3, 5, 6, 2, 4]
print(array)
random.shuffle(array)
print(array)

median = select(array, 0, len(array) - 1, (len(array) - 1) / 2)
# array.sort()
print(median)
