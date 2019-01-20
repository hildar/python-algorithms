# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках
# домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

# Задача из предыдущего ДЗ.
# Определить, какое число в массиве встречается чаще всего.

import random
import cProfile


# Вариант 1
def version_1(MAX_ITEM):
    SIZE = 20
    MIN_ITEM = -10
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
    return max_num + MIN_ITEM


# python -m timeit -n 100 -s "import task_1" "task_1.version_1(1000)"
#
# 100 loops, best of 5: 122 usec per loop - 1 000
# 100 loops, best of 5: 209 usec per loop - 2 000
# 100 loops, best of 5: 302 usec per loop - 3 000
# 100 loops, best of 5: 555 usec per loop - 6 000
# 100 loops, best of 5: 906 usec per loop - 10 000
# 100 loops, best of 5: 8.99 msec per loop -100 000
# 100 loops, best of 5: 110 msec per loop - 1 000 000


# cProfile.run('version_1(1000)')
#
# 1    0.000    0.000    0.000    0.000 task_1.py:8(version_1) -               1 000
# 1    0.001    0.001    0.001    0.001 task_1.py:8(version_1) -               10 000
#
# 1    0.004    0.004    0.004    0.004 task_1.py:12(<listcomp>)
# 1    0.006    0.006    0.010    0.010 task_1.py:8(version_1) -               100 000
#
# 1    0.055    0.055    0.055    0.055 task_1.py:12(<listcomp>)
# 1    0.055    0.055    0.110    0.110 task_1.py:8(version_1) -               1 000 000
#
# 1    0.113    0.113    0.113    0.113 task_1.py:12(<listcomp>)
# 1    0.112    0.112    0.226    0.226 task_1.py:8(version_1) -               2 000 000
#
# 1    0.562    0.562    0.562    0.562 task_1.py:13(<listcomp>)
# 1    0.557    0.557    1.119    1.119 task_1.py:7(version_1) -               10 000 000
#
# Запуск с небольшим изменением SIZE для сравнения с вариантом № 4
# cProfile.run('version_1(30)')
# SIZE = 1000000
# 1    0.291    0.291    2.229    2.229 task_1.py:11(<listcomp>)

#
#
# На первый взгляд сложность алгоритма линейная O(n). Видно увеличение затрачиваемых ресурсов на
# строчке № 13 - наполнение второго массива для индексов. Но это до тех пор пока размер
# первого массива без изменений.
# Вообще, по скорости этот алгоритим идентичен четвертому варианту. Как вы и сказали затрачивается
# память, но скорость выполнения коллосальная
#
#


# Вариант 2
def version_2(MAX_ITEM):
    SIZE = 20
    MIN_ITEM = -10
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    num = array[0]
    frequency = 1
    for i in range(len(array)):
        spam = 1
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                spam += 1
        if spam > frequency:
            frequency = spam
            num = array[i]
    if frequency > 1:
        return num
    else:
        return False


# python -m timeit -n 100 -s "import task_1" "task_1.version_2(1000)"
#
# 100 loops, best of 5: 57.3 usec per loop - 1 000
# 100 loops, best of 5: 57.7 usec per loop - 2 000
# 100 loops, best of 5: 56.6 usec per loop - 3 000
# 100 loops, best of 5: 57.1 usec per loop - 6 000
# 100 loops, best of 5: 55.7 usec per loop - 1 000 000


# cProfile.run('version_2(100000000000000000000000000000000000)')
# 1    0.000    0.000    0.000    0.000 task_1.py:69(version_2) - 100000000000000000000000000000000000

#
#
# Сразу видно как я налажал при выполнении предыдущей домашки. Коллосальные затраты были на
# второй массив используемый только для хранения индексов.
#
#


# Вариант 3. Попробуем изменять размер первого массива со второго варианта выполнения ДЗ
def version_3(SIZE):
    MIN_ITEM = -10
    MAX_ITEM = 30
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    num = array[0]
    frequency = 1
    for i in range(len(array)):
        spam = 1
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                spam += 1
        if spam > frequency:
            frequency = spam
            num = array[i]
    if frequency > 1:
        return num
    else:
        return False


# python -m timeit -n 100 -s "import task_1" "task_1.version_3(10)"
#
# 100 loops, best of 5: 25 usec per loop - 10
# 100 loops, best of 5: 75.5 usec per loop - 25
# 100 loops, best of 5: 199 usec per loop - 50
# 100 loops, best of 5: 267 usec per loop - 60
# 100 loops, best of 5: 345 usec per loop - 70
# 100 loops, best of 5: 632 usec per loop - 100
# 100 loops, best of 5: 2.05 msec per loop - 200
# 100 loops, best of 5: 12.7 msec per loop - 500
# 100 loops, best of 5: 50.3 msec per loop - 1000


# cProfile.run('version_3(1000)')
#
# 1000    0.000    0.000    0.002    0.000 random.py:218(randint)
# 1    0.050    0.050    0.052    0.052 task_1.py:110(version_3) -                 1 000
# 1    0.199    0.199    0.203    0.203 task_1.py:110(version_3) -                 2 000
# 1    0.443    0.443    0.450    0.450 task_1.py:110(version_3) -                 3 000
# 1    1.247    1.247    1.258    1.258 task_1.py:110(version_3) -                 5 000
# 1    1.799    1.799    1.813    1.813 task_1.py:110(version_3) -                 6 000
# 1    4.978    4.978    5.001    5.001 task_1.py:110(version_3) -                 10 000


#
#
# Сложность алгоритма O(3*n). Не совсем понимаю почему так, т.к. ожидал квадратичное
# увеличение сложности.
#
#


# Вариант 4. Попробуем со словарем
def version_4(SIZE):
    MIN_ITEM = -10
    MAX_ITEM = 30
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    counter = {}
    num = None
    frequency = 1
    for item in array:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
        if counter[item] > frequency:
            frequency = counter[item]
            num = item

    if num is not None:
        return num
    else:
        return False


aaa = 0  # Это чтобы убрать бисючие полоски :-( Вот попробуйте закоментировать строку

# python -m timeit -n 100 -s "import task_1" "task_1.version_4(100)"
#
# 100 loops, best of 5: 173 usec per loop - 100
# 100 loops, best of 5: 350 usec per loop - 200
# 100 loops, best of 5: 530 usec per loop - 300
# 100 loops, best of 5: 705 usec per loop - 400
# 100 loops, best of 5: 881 usec per loop - 500
# 100 loops, best of 5: 1.76 msec per loop - 1 000
# 100 loops, best of 5: 8.82 msec per loop - 5 000
# 100 loops, best of 5: 17.6 msec per loop - 10 000


# cProfile.run('version_4(2000000)')
#
# 10000    0.003    0.000    0.020    0.000 random.py:218(randint)
# 1    0.002    0.002    0.024    0.024 task_1.py:163(version_4) -             10 000
# 1    0.003    0.003    0.022    0.022 task_1.py:166(<listcomp>)
#
# 1    0.021    0.021    0.244    0.244 task_1.py:163(version_4)
# 1    0.027    0.027    0.222    0.222 task_1.py:166(<listcomp>) -            100 000
#
# 1    0.044    0.044    0.498    0.498 task_1.py:163(version_4)
# 1    0.058    0.058    0.454    0.454 task_1.py:166(<listcomp>) -            200 000
#
# 1    0.220    0.220    2.484    2.484 task_1.py:163(version_4)
# 1    0.294    0.294    2.265    2.265 task_1.py:166(<listcomp>) -            1 000 000
#
# 1    0.441    0.441    5.000    5.000 task_1.py:163(version_4) -             2 000 000
#


#
#
# Сложность алгоритма линейная O(n). Наилучшая скорость выполнения, как и вариант 1.
# Больше всего ресурсов уходит на наполнение массива array.
#
