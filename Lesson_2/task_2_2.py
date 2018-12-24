# Задача № 2_2 (Рекурсивно)
# Сформировать из введенного числа обратное по порядку входящих в него цифр и
# вывести на экран. Например, если введено число 3486, то надо вывести число 6843.


# Рекурсию явно сложнее продумать, чем цикл
def func_reverse(num):
    # Если цифра одна или последняя, то сразу её и возвращаем
    if num // 10 == 0:  # Базовый случай
        return num
    elif num != 0:
        return str(num % 10) + str(func_reverse(num // 10))


print('Задача № 2 (Рекурсивно).')
num_input = int(input('Введите любое натуральное число: '))

revers = int(func_reverse(num_input))

print(f'Обратное числу {num_input} по порядку входящих в него цифр: {revers}')
