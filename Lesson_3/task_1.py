# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны любому из чисел в диапазоне от 2 до 9.

# SIZE = 98
MIN_ITEM = 2
MAX_ITEM = 99
# array = [_ for _ in range(MIN_ITEM,MAX_ITEM)]  # по сути массив не обязательно создавать
int_2, int_3, int_4, int_5, int_6, int_7, int_8, int_9, = 0, 0, 0, 0, 0, 0, 0, 0

for i in range(MIN_ITEM,MAX_ITEM):
    if i % 2 == 0:
        int_2 += 1
    if i % 3 == 0:
        int_3 += 1
    if i % 4 == 0:
        int_4 += 1
    if i % 5 == 0:
        int_5 += 1
    if i % 6 == 0:
        int_6 += 1
    if i % 7 == 0:
        int_7 += 1
    if i % 8 == 0:
        int_8 += 1
    if i % 9 == 0:
        int_9 += 1


print(f'В диапазоне чисел от {MIN_ITEM} до {MAX_ITEM} кратны любому от 2 до 9:\n'
      f'2 = {int_2}\n3 = {int_3}\n4 = {int_4}\n5 = {int_5}\n6 = {int_6}\n'
      f'7 = {int_7}\n8 = {int_8}\n9 = {int_9}')
