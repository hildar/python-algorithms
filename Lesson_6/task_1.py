# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках
#  первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным
# использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода
# для одной и той же задачи. Результаты анализа вставьте в виде комментариев к коду.
# Также укажите в комментариях версию Python и разрядность вашей ОС.
# Python 3.

# Задача № 1
# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

import sys


def func_cnt(num):
    cnt_odd = 0
    cnt_parity = 0

    while num != 0:
        if num % 2 == 0:
            cnt_parity += 1
        else:
            cnt_odd += 1
        num //= 10

    return cnt_odd, cnt_parity


print('Задача № 1.')
num_input = int(input('Введите любое натуральное число: '))

num_odd, num_parity = func_cnt(num_input)

print(f'Число {num_input} имеет\n'
      f'четных цифр: {num_parity}\n'
      f'нечетных цифр: {num_odd}')



# Начал реализацию ДЗ
a = [str(i) for i in range(4)]


def show_size(x, sum):
    if not hasattr(x, '__iter__'):
        return sys.getsizeof(x)
    elif isinstance(x, str):
        return sys.getsizeof(x)
    else:
        if not isinstance(x, str):
            for item in x:
                return sum + show_size(item, sum)


def show_size_print(x):
    print(sys.getsizeof(x), type(x))
    if hasattr(x, '__iter__'):
        if not isinstance(x, str):
            for item in x:
                show_size_print(item)


sum=0
print(show_size(a, sum))
print(show_size_print(a))