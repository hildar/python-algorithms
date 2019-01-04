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
