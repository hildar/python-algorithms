# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import random


# пузырьковая сортировка
def bubble_sort(array):
    n = 1
    # Добавим переменную len_arr чтобы проходить каждый проход на один элемент меньше, пузырек же уже всплыл
    len_arr = len(array)
    while n < len(array):
        check = 0  # Добавим проверку обменов чтобы небыло лишних проходов
        for i in range(len_arr - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                check = 1
        if check == 0:
            break
        n += 1
        len_arr -= 1
        # print(array)


array = [i for i in range(-100, 100)]
random.shuffle(array)
print(array)

bubble_sort(array)
print(array)
