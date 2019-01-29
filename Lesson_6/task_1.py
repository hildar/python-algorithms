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

    return cnt_odd, cnt_parity, locals()


print('Задача № 1.')
num_input = int(input('Введите любое натуральное число: '))

num_odd, num_parity, loc1 = func_cnt(num_input)

print(f'Число {num_input} имеет\n'
      f'четных цифр: {num_parity}\n'
      f'нечетных цифр: {num_odd}')

print(f'loc1 = {loc1}')



# Начал реализацию ДЗ


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


# # тесты
# d = [1, 2, '3', ['01', 1, 2.22, [1, 2, '23', 3, '34', '45']]]
# print(f'd = {d}')
# print('show_sizeof(d) = 750 == ', show_sizeof(d))
#
# e = [str(i) for i in range(3)]
# f = set([str(i) for i in range(2)])
# e.append(f)
# print('e = ', e)
# print('show_sizeof(e) = 570 == ', show_sizeof(e))
#
# g = {str(i): i for i in range(3)}
# print('g = ', g)
# print('show_sizeof(g) = 662 == ', show_sizeof(g))
#
# print(show_sizeof(3))
# print(show_sizeof('3'))
# print(show_sizeof(3.0))
# print(show_sizeof(None), sys.getsizeof(None))
# print(show_sizeof(True), sys.getsizeof(True))
# print('inf', show_sizeof(float('inf')), sys.getsizeof(float('inf')))

glob = globals()
print(glob)
# print('show_sizeof(loc) == ', show_sizeof(loc))
