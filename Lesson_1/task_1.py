# Задача № 1
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь

num = int(input("Введите целое трехзначное число: "))
tmp = num  # сохраним переменную чтобы при выводе не использовать конкатенацию

a = num % 10
num = num // 10
b = num % 10
num = num // 10
c = num % 10

print(f"Сумма цифр числа {tmp} = {a + b + c}")
print(f"Произведение цифр числа {tmp} = {a * b * c}")
