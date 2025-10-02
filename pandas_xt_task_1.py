# Задание 1
# Для датафрейма log из материалов занятия создайте столбец source_type по правилам:

# если источник traffic_source равен Yandex или Google, то в source_type ставится organic;
# для источников paid и email из России ставим ad;
# для источников paid и email не из России ставим other;
# все остальные варианты берём из traffic_source без изменений.

import pandas as pd
import numpy as np
log = pd.read_csv('visit_log.csv', sep=';')
print(log.head())
print()

log['source_type'] = log['traffic_source']
log.loc[(log['traffic_source'] == 'yandex') | (log['traffic_source'] == 'google'), 'source_type'] = 'organic'
log.loc[(log['region'] == 'Russia') & ((log['traffic_source'] == 'paid') | (log['traffic_source'] == 'email')), 'source_type'] = 'ad'
log.loc[(log['region'] != 'Russia') & ((log['traffic_source'] == 'paid') | (log['traffic_source'] == 'email')), 'source_type'] = 'other'
print(log.head(n=10))
print()
print(log.tail(n=10))
