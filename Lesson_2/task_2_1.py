# Задача № 2_1
# Сформировать из введенного числа обратное по порядку входящих в него цифр и
# вывести на экран. Например, если введено число 3486, то надо вывести число 6843.


def func_reverse(num):
    reverse = ''

    if num != 0:
        while num != 0:
            reverse = reverse + str(num % 10)
            num //= 10
    else:
        reverse = 0;

    return int(reverse)


print('Задача № 2.')
num_input = int(input('Введите любое натуральное число: '))

revers = func_reverse(num_input)

print(f'Обратное числу {num_input} по порядку входящих в него цифр: {revers}')
