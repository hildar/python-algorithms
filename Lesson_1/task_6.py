# Задача № 6
# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше
# другого).

a = int(input('Введите первое целое число: '))
b = int(input('Введите второе целое число: '))
c = int(input('Введите третье целое число: '))

if a < b < c or c < b < c:
    var = b
elif b < a < c or c < a < b:
    var = a
else:
    var = c

print(f'Число {var} является средним')
