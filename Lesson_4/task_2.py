# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.

import cProfile


#  Вариант 1. Без использования алгоритма «Решето Эратосфена».


def notSieve(n):
    lst = [2]
    for i in range(3, n * n, 2):  # Делаем последовательность заведомо бОльшую
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
        if len(lst) >= n + 1:  # Выход, если превышен i-й по счету элемент
            break
    return lst[n]


# python -m timeit -n 100 -s "import task_2" "task_2.notSieve(100)"
#
# 100 loops, best of 5: 207 usec per loop -   100
# 100 loops, best of 5: 536 usec per loop -   200
# 100 loops, best of 5: 964 usec per loop -   300
# 100 loops, best of 5: 1.43 msec per loop -  400
# 100 loops, best of 5: 1.96 msec per loop -  500
# 100 loops, best of 5: 5.17 msec per loop -  1000


# cProfile.run('notSieve(10000)')
#
# 1    0.134    0.134    0.137    0.137 task_2.py:12(notSieve) -                    10 000
# 41898    0.002    0.000    0.002    0.000 {built-in method builtins.len} - вызов len аж 41898 раз!
#
# 1    0.348    0.348    0.354    0.354 task_2.py:12(notSieve) -                    20 000
# 89898    0.005    0.000    0.005    0.000 {built-in method builtins.len} - 89898 - это критично?
#
# 1    0.628    0.628    0.638    0.638 task_2.py:12(notSieve) -                    30 000
# 140153    0.009    0.000    0.009    0.000 {built-in method builtins.len}
#
# 1    0.933    0.933    0.947    0.947 task_2.py:12(notSieve) -                    40 000
# 191976    0.012    0.000    0.012    0.000 {built-in method builtins.len}
#
# 1    1.237    1.237    1.255    1.255 task_2.py:12(notSieve) -                    50 000
# 244783    0.015    0.000    0.015    0.000 {built-in method builtins.len}
#
# 1    3.282    3.282    3.321    3.321 task_2.py:12(notSieve) -                    100 000
# 519889    0.033    0.000    0.033    0.000 {built-in method builtins.len}


# Сложность алгоритма O(2.6 * n)
#



# Вариант 2. Используя «Решето Эратосфена».


def isSieve(n):
    m = n * 100  # Увеличиваем пространство для маневра. Если честно,
    # то я не успел найти способа лучше (в очереди ДЗ по параллельному курсу)
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, m):
        if sieve[i] != 0:
            j = i + i
            while j < m:
                while len(sieve) <= m:
                    sieve.append(len(sieve))
                sieve[j] = 0
                j += i
    result = [i for i in sieve if i != 0]
    return result[n]


# python -m timeit -n 100 -s "import task_2" "task_2.isSieve(100)"
#
# 100 loops, best of 5: 759 usec per loop -   10
# 100 loops, best of 5: 1.55 msec per loop -  20
# 100 loops, best of 5: 2.39 msec per loop -  30
# 100 loops, best of 5: 3.2 msec per loop -   40
# 100 loops, best of 5: 4.26 msec per loop -  50
# 100 loops, best of 5: 8.34 msec per loop - 100
# 100 loops, best of 5: 17.1 msec per loop - 200


# cProfile.run("isSieve(10000)")
#
# 1    1.162    1.162    1.547    1.547 task_2.py:70(isSieve) -                     10 000
# 4755210    0.279    0.000    0.279    0.000 {built-in method builtins.len} - 4755210 - вот это я
# понимаю уничтожение памяти
#
# 1    2.401    2.401    3.182    3.182 task_2.py:70(isSieve) -                     20 000
# 9619867    0.569    0.000    0.569    0.000 {built-in method builtins.len}
#
# 1    3.650    3.650    4.828    4.828 task_2.py:70(isSieve) -                     30 000
# 14521892    0.860    0.000    0.860    0.000 {built-in method builtins.len}
#
# 1    4.913    4.913    6.482    6.482 task_2.py:70(isSieve) -                     40 000
# 19447433    1.142    0.000    1.142    0.000 {built-in method builtins.len}
#
# 1    6.118    6.118    8.079    8.079 task_2.py:70(isSieve) -                     50 000
# 24389913    1.440    0.000    1.440    0.000 {built-in method builtins.len}
# 1   12.427   12.427   16.370   16.370 task_2.py:70(isSieve) -                     100 000
# 49265738    2.892    0.000    2.892    0.000 {built-in method builtins.len}


# Алгоритм имеет сложность O(n). Но при этом оочень медленно выполнятеся, в десять раз медленнее
# предыдущего. Возможно это связано с кривыми руками.
#