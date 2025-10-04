# Задание 4
# Дана статистика услуг перевозок клиентов компании по типам 
# (см. файл “Python_13_join.ipynb” в разделе «Материалы для лекции “Продвинутый pandas”» ---- 
# Ноутбуки к лекции «Продвинутый pandas»).
# Нужно сформировать две таблицы:

# таблицу с тремя типами выручки для каждого client_id без указания адреса клиента;
# аналогичную таблицу по типам выручки с указанием адреса клиента.
# Обратите внимание, что в процессе объединения таблиц данные не должны теряться.

# К домашнему заданию №4
# Дана статистика услуг перевозок клиентов компании по типам:

# rzd - железнодорожные перевозки
# auto - автомобильные перевозки
# air - воздушные перевозки
# client_base - адреса клиентов

import pandas as pd

rzd = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115],
        'rzd_revenue': [1093, 2810, 10283, 5774, 981]
    }
)
print(rzd.head(), '\n')

air = pd.DataFrame(
    {
        'client_id': [115, 116, 117, 118],
        'air_revenue': [81, 4, 13, 173]
    }
)
print(air.head(), '\n')

client_base = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115, 116, 117, 118],
        'address': ['Комсомольская 4', 'Энтузиастов 8а', 'Левобережная 1а', 'Мира 14', 'ЗЖБИиДК 1',
                    'Строителей 18', 'Панфиловская 33', 'Мастеркова 4']
    }
)
print(client_base.head(), '\n')

# чтобы клиенты не потерялись, сделаем outer-join обеих таблиц с перевозками
revenue_without_clientaddress = pd.merge(rzd, air, on='client_id', how='outer')
print(revenue_without_clientaddress, '\n')

# в базе данных есть все клиенты. поэтому сделаем объединение по client_base слева.
revenue_with_clientaddress = pd.merge(client_base, revenue_without_clientaddress, on='client_id', how='left')
print(revenue_with_clientaddress, '\n')
