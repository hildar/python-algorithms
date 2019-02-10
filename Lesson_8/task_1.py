# 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

import hashlib


# Функция поиска подстрок в строке
def subs_count(string):
    # Создаем множество для хранения хешей чтобы проще было проверять подстроки
    hash_list = set()
    # И добавляем туда первые два элемента которые не будут являтся подстрокой
    # это сама строка и пустая строка
    hash_list.add(hashlib.sha1(string.encode('utf-8')).hexdigest())
    hash_list.add(hashlib.sha1(''.encode('utf-8')).hexdigest())

    # Для наглядности будем записывать уникальные подстроки в массив subs_list
    subs_list = []
    counter = 0

    for i in range(len(string) + 1):
        for j in range(len(string) + 1):
            spam = string[i:j]
            subs = hashlib.sha1(spam.encode('utf-8')).hexdigest()
            if subs not in hash_list:
                subs_list.append(spam)
                counter += 1
            hash_list.add(subs)

    return counter, subs_list


s1 = input('Введите строку: ')
str_cnt, str_lst = subs_count(s1)
print(f'\nВ введенной строке {str_cnt} подстрок:\n{str_lst}')
