# Задача № 3
# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.


def func_sum(n):
    MULTIPLE = -0.5
    row = 1
    sum_row = 0

    while n != 0:
        sum_row += row
        row *= MULTIPLE
        n -= 1

    return sum_row


print('Задача № 3.')
n_input = int(input('Введите любое натуральное число: '))

summ = func_sum(n_input)

print(f'Сумма ряда чисел "1 -0.5 0.25 -0.125 ..." с {n_input} элементами = {summ}')