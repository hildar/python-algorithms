# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

import random


# Функция разбиения массива и поиска опорного индекса
def partition(array, first, last):
    # Добавим элемент случайности выбора для того чтобы время поиска было в среднем O(n * log(n))
    q = random.randrange(first, last + 1)
    array[q], array[last] = array[last], array[q]

    # Для удобства за опорный элемент принимаем последний
    pivot = array[last]
    i = first - 1

    for j in range(first, last):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[last] = array[last], array[i + 1]

    # возвращаем индекс опорного элемента
    return i + 1


# Функция выбора (поиск медианы - частный случай)
def select(array, first, last, i):
    # base case
    if first == last:
        return array[first]

    q = partition(array, first, last)
    k = q - first + 1   # Множество левой части разбиения плюс один опорный элемент

    if i == k:
        return array[q]  # Ответом является опорное значение
    elif i < k:
        return select(array, first, q - 1, i)  # Ищем в левой части массива
    else:
        return select(array, q + 1, last, i - k)  # Иначе в правой части массива


m = int(input('Введите натуральное целое число m. Размерность массива будет согласно формуле (2 * m + 1) : '))

array = [random.randrange(0, 100) for i in range(2 * m + 1)]
print(array)

# Т.к. медиана по математическому порядку считается с одного то и индекс ищем на один больше
i = (len(array) + 1) / 2

median = select(array, 0, len(array) - 1, i)
print(f'median = {median}')

# for check:
# array.sort()
# print(array)
