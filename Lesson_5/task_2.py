# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


from collections import deque

BASE = 16

# Базовый словарь шестнадциатиричной системы
hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
            '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

# Реверсивный словарь шестнадциатиричной системы
hex_dict_reverse = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
                    '10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}


# Функция сложения
# def summ_hex(n1, n2):
#     # Выявление наиболее длинного числа
#     if len(n1) > len(n2):
#         len_sum = len(n1)
#     else:
#         len_sum = len(n2)
#
#     # Цикл сложения
#     digit = 0
#     spam_summ = deque()
#     for i in range(len_sum):
#         key1 = n1.pop() if len(n1) != 0 else '0'
#         key2 = n2.pop() if len(n2) != 0 else '0'
#         spam = hex_dict[key1] + hex_dict[key2]
#
#         # Увеличиваем разряд если предыдущее сложение было больше базы
#         spam += 1 if digit != 0 else False
#
#         # Добавляем элемент в результирующий массив сложения 'summ' и
#         # выставляем необходимость увеличения разряда
#         if spam >= BASE:
#             spam_summ.appendleft(hex_dict_reverse[str(spam - 16)])
#             digit = 1
#         else:
#             spam_summ.appendleft(hex_dict_reverse[str(spam)])
#             digit = 0
#
#         # Добавление последнего разряда
#         len_sum -= 1
#         if len_sum == 0 and digit != 0:
#             spam_summ.appendleft(str(digit))
#
#     return spam_summ

# Функция сложения
def summ_hex(n1, n2):
    # Выявление наиболее длинного числа
    if len(n1) > len(n2):
        len_sum = len(n1)
    else:
        len_sum = len(n2)

    # Цикл сложения
    digit = 0
    spam_summ = deque()
    for i in range(len_sum):
        key1 = n1[len(n1) - i - 1] if (len(n1) - i) > 0 else '0'
        key2 = n2[len(n2) - i - 1] if (len(n2) - i) > 0 else '0'

        spam = hex_dict[key1] + hex_dict[key2]

        # Увеличиваем разряд если предыдущее сложение было больше базы
        spam += 1 if digit != 0 else False

        # Добавляем элемент в результирующий массив сложения 'spam_summ' и
        # выставляем необходимость увеличения разряда
        if spam >= BASE:
            spam_summ.appendleft(hex_dict_reverse[str(spam - 16)])
            digit = 1
        else:
            spam_summ.appendleft(hex_dict_reverse[str(spam)])
            digit = 0

        # Добавление последнего разряда
        if i == len_sum - 1 and digit != 0:
            spam_summ.appendleft(str(digit))

    return spam_summ


# Функция умножения
def mult_hex(n1, n2):
    spam_summ = deque()
    spam_summ_last = deque()
    for i in range(len(n1)):
        digit = 0
        key1 = n1[len(n1) - 1 - i]
        for j in range(len(n2)):
            key2 = n2[len(n2) - 1 - j]
            spam = hex_dict[key1] * hex_dict[key2] + digit

            # Добавляем элемент во временный массив умножения 'spam_summ' и
            # выставляем значение разряда

            if spam >= BASE:
                spam_summ.appendleft(hex_dict_reverse[str(spam % BASE)])
                digit = spam // BASE
            else:
                spam_summ.appendleft(hex_dict_reverse[str(spam)])
                digit = 0
            if j == len(n2) - 1:
                spam_summ.appendleft(hex_dict_reverse[str(digit)])

        if i != 0:
            for item in range(i):
                spam_summ.append('0')

        spam_summ_last = summ_hex(spam_summ_last, spam_summ)
        spam_summ.clear()

    return spam_summ_last


# Преобразовываем в очередь
a2 = deque(str('a2').upper())
a2b = deque(str('a2b').upper())
c4f = deque(str('c4f').upper())
ff = deque(str('ff').upper())

print('sum =', summ_hex(a2, c4f))
print('sum =', summ_hex(a2b, c4f))
print('sum =', summ_hex(ff, ff))

print('mult =', mult_hex(a2, c4f))
print('mult =', mult_hex(a2b, c4f))
print('mult =', mult_hex(ff, ff))

print('\nА теперь сами')
number1 = deque(str(input('Введите первое шестнадцатиричное число: ')).upper())
number2 = deque(str(input('Введите второе шестнадцатиричное число: ')).upper())
print('sum =', summ_hex(number1, number2))
print('mult =', mult_hex(number1, number2))
