# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и
# отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple

Company = namedtuple('Company', 'name, quarter_1, quarter_2, quarter_3, quarter_4, average')
companys = []

# Данные для автотестов
# Tesla = Company('Тесла', 40, 30, 45, 65, 0)
# SpaceX = Company('Спэйс-икс', 30, 25, 20, 35, 0)
# NeuroLink = Company('Нейролинк', 10, 15, 25, 20, 0)
# SolarCity = Company('СоларСити', 60, 90, 40, 80, 0)
# Boring = Company('Боринг', 40, 20, 40, 35, 0)
# companys = [Tesla, SpaceX, NeuroLink, SolarCity, Boring]

print('Введите данные компаний.')
count_companys = int(input('Введите количество компаний которые вы собираетесь ввести: '))
# count_companys = 2
for i in range(count_companys):
    spam = []
    spam.append(str(input(f'Введите имя компании № {i + 1}: ')))
    spam.append(int(input('Введите прибыль за первый квартал: ')))
    spam.append(int(input('Введите прибыль за второй квартал: ')))
    spam.append(int(input('Введите прибыль за третий квартал: ')))
    spam.append(int(input('Введите прибыль за четвертый квартал: ')))
    companys.append(Company(spam[0], spam[1], spam[2], spam[3], spam[4], 0))

# Вычисляем среднегодовую прибыль по предприятиям
common_average = 0
for i in range(len(companys)):
    spam = companys[i].quarter_1 + companys[i].quarter_2 + companys[i].quarter_3 + companys[i].quarter_4
    companys[i] = companys[i]._replace(average=spam)
    common_average += companys[i].average

# Вычисляем среднюю прибыль по всем предприятиям
if len(companys) != 0:
    common_average /= len(companys)

below = []  # Ниже среднего
above = []  # Выше среднего
# для удобчтва разбиваем на два массива
for i in companys:
    if i.average < common_average:
        below.append(i)
    else:
        above.append(i)

print(f'\nНиже среднего:')
for i in below:
    print(i.name)

print(f'\nВыше среднего:')
for i in above:
    print(i.name)
