# Задание 3
# Используйте файл с оценками фильмов ml-latest-small/ratings.csv. 
# Посчитайте среднее время жизни пользователей, которые выставили более 100 оценок. 
# Под временем жизни понимается разница между максимальным и минимальным 
# значениями столбца timestamp для данного значения userId.

import pandas as pd

def groupby_for_timestamp(data):
    return data.timestamp.max() - data.timestamp.min()


ratings = pd.read_csv('ml-latest-small/ratings.csv')
print('\nПЕЧАТАЕМ ИСХОДНУЮ ТАБЛИЦУ РЕЙТИНГОВ')
print(ratings.head(n=10))
# группируем по userId
# считаем количество их оценок и даты первой и последней проставленных оценок
group_user = ratings.groupby('userId').agg({'userId':'count','timestamp':['min','max']})
print('\nСГРУППИРОВАННАЯ ПО ПОЛЬЗОВАТЕЛЯМ ТАБЛИЦА С ПОЛЯМИ МАКСИМАЛЬНОГО И МИНИМАЛЬНОГО ВРЕМЕНИ ПРОСТАВЛЕНИЯ ОЦЕНОК')
print(group_user.head(10))

group_user_ratings = group_user.loc[group_user['userId']['count'] > 100]
print('\nСГРУППИРОВАННАЯ ПО ПОЛЬЗОВАТЕЛЯМ ТАБЛИЦА, ГДЕ ТОЛЬКО ПОЛЬЗОВАТЕЛИ С КОЛИЧЕСТВОМ ОЦЕНОК БОЛЬШЕ СТА')
print(group_user_ratings.head(10))

group_user_ratings['timestamp_diff'] = group_user_ratings['timestamp']['max'] - group_user_ratings['timestamp']['min']
print(group_user_ratings.head(10))

seconds_in_day = 86_400
group_user_ratings['avg_time_in_days'] = group_user_ratings['timestamp_diff'].mean() / seconds_in_day
print(group_user_ratings.head(10))

print('\nСреднее время жизни пользователей, которые поставили более 100 оценок:', group_user_ratings['timestamp_diff'].mean() / seconds_in_day, 'дней')
