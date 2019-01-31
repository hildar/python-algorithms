# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны любому из чисел в диапазоне от 2 до 9.

# SIZE = 98
MIN_ITEM = 2
MAX_ITEM = 99
MIN_MULT = 2  # multiplicity of numbers - кратность числа
MAX_MULT = 9
array = [0 for _ in range(MIN_MULT, MAX_MULT + 1)]

for i in range(MIN_ITEM, MAX_ITEM):
    for j in range(MIN_MULT, MAX_MULT + 1):
        if i % j == 0:
            array[j - MIN_MULT] += 1

print(f'В диапазоне чисел от {MIN_ITEM} до {MAX_ITEM}, кратные любому из чисел от 2 до 9:')
for i, item in enumerate(array):
    print(f'{i + MIN_MULT} = {item}')



import sys

# ******************************** Home work **********************************
#
#
# Функция для проверки памяти
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


array_var = [MIN_ITEM, MAX_ITEM, MIN_MULT, MAX_MULT, array]
print(f'total memory = {show_sizeof(array_var)} byte')
# Python 3.7.2, Разрядность - x64
