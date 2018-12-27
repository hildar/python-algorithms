# Задача № 1
# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


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
