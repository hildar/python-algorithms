# Задача № 4
# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32
# и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

num_code = 32
LAST_CODE = 127
pair = 10
row = ''

while num_code <= LAST_CODE:
    row = f'{row}  "{num_code} - {chr(num_code)}"'
    num_code += 1
    pair -= 1

    if pair == 0:
        row = f'{row}\n'
        pair = 10

print('Задача № 4.')
print(row)
