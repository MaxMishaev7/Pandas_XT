# Задание 2
# В файле URLs.txt содержатся URL страниц новостного сайта. 
# Вам нужно отфильтровать его по адресам страниц с текстами новостей. 
# Известно, что шаблон страницы новостей имеет внутри URL конструкцию: /, затем 8 цифр, затем дефис. 
# Выполните действия:
# Прочитайте содержимое файла в датафрейм.
# Отфильтруйте страницы с текстом новостей, используя метод str.contains и регулярное выражение в соответствие с заданным шаблоном.

import pandas as pd

urls = pd.read_csv('URLs.txt')
print(urls.head(n=10))
print()

url_series = urls['url']
urls_filter = url_series.str.contains('/\d{8}-', regex=True)
print(urls_filter.head(n=10))

print(urls[urls['url'].str.contains('/\d{8}-', regex=True)].head(10))
print()
print(urls[urls['url'].str.contains('/\d{8}-', regex=True)].tail(10))

