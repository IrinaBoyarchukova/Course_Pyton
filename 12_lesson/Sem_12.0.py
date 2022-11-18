# -*- coding: utf-8 -*-

# -- Sheet --

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

# считываем данные из csv файла с помощью pandas
df = pd.read_csv("Video_Games.csv", sep=",")

# выводим информацию о таблице
print(df.info())
display(df.describe())

# Приведем названия столбцов к нижнему регистру

print(df.columns)
columns = []
for c in df.columns:
    columns.append(c.lower())
df.columns = columns
print(df.columns)

# Отобразим результат изменений
# Выведем только первые несколько строчек

df.head(2)

# Поменяем у стлобца год тип на целочисленный

df['year_of_release'] = df['year_of_release'].astype('Int64')
df['year_of_release'].dtype

# Создадим столбец sales - сумма продаж во всех регионах 

df['sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales'] + df['other_sales']
df.head(12)

# Сколько игр выпускалось в разные годы.

time_release = df.groupby('year_of_release')['name'].count().reset_index()
time_release.columns = ['year', 'quantity']
time_release

# Кол-во релизов по годам

plt.figure(figsize=(14, 5))
plt.bar(time_release['year'], time_release['quantity'], label='Кол-во релизов за год', color='g', alpha=0.85, width=0.9)
plt.xlabel('Год релизов')
plt.ylabel('Кол-во релизов')
plt.grid()
plt.title(f'Кол-во релизов по годам')
plt.show()

# Анализ продаж по платформам

plf = df.groupby('platform')['sales'].sum().sort_values().reset_index()
plf

popul_platforms = plf.loc[17:30, 'platform'].values
popul_platforms

color = ['r','b','y','black','c','orange','grey','green','brown','purple','m','pink','yellow','coral','darkcyan','dimgray','lime']

plt.figure(figsize=(15, 6))
plt.grid()
plt.title('Объёмы продаж на разных платформах по годам')

mean_year_life = 0
for i in range(0,len(popul_platforms)):
    platform  = df.query('platform == @popul_platforms[@i]').groupby('year_of_release')['sales'].sum()
    mean_year_life += platform.count()
    platform.plot(x=platform.index, y=platform.values, style='-^', color=color[i],
                  label=popul_platforms[i], alpha=0.8, grid=True)
plt.xlabel('Расчетный год')    
plt.ylabel('Объём продаж за год')
plt.legend()
plt.show()

# Cредняя жизнь платформы
mean_year_life/len(popul_platforms)

platform2017 = df.pivot_table(index='year_of_release', columns='platform', values='sales', aggfunc='sum').\
    query('year_of_release>2004').fillna(0).reset_index()
platform2017['year_of_release'] = platform2017['year_of_release'].astype('Int64')

for column in platform2017.columns:
    if platform2017[column].sum()==0:
        platform2017.drop(column, axis=1,inplace=True)

display(platform2017)

#Построение графика 
plt.figure(figsize=(15, 7))
plt.grid()
plt.title('Объёмы продаж на разных платформах по годам')

i=0
for column in platform2017.columns[1:]:
    plt.plot(platform2017['year_of_release'].to_list(), platform2017[column].to_list(), label=column, color=color[i], alpha=0.95);
    i+=1 

plt.grid()
plt.xlabel('Расчетный год')    
plt.ylabel('Объём продаж за год')
plt.legend()
plt.show()

op5_2017 = ['PS4', 'XOne', 'WiiU', 'PSV', '3DS']

top2005 = df.query('year_of_release>=2005').groupby('platform')['sales'].sum().sort_values(ascending=False).reset_index().head(10)
top2005

fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8) = plt.subplots(nrows=1, ncols=8, figsize=(16, 12))
fig.autofmt_xdate()

p = {ax1:'X360', ax2:'PS3', ax3:'Wii', ax4:'DS', ax5:'PS2', ax6:'PS4', ax7:'PSP', ax8:'3DS'}
for ax in [ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8]:
    sales = df.query('platform==@p[@ax] and sales<1.5')['sales']
    ax.boxplot(sales)
    ax.grid()
    ax.set_title(p[ax])

fig.autofmt_xdate()

one_pl = df.query('platform=="X360"')[['sales', 'critic_score', 'user_score']].dropna().reset_index(drop=True)
one_pl



print('Коэффициент Зависимости Продаж от отзывов критиков =' , one_pl['sales'].corr(one_pl['critic_score']))
one_pl.plot(x='critic_score',y='sales',kind='scatter',figsize=(15,5), alpha=0.5)
plt.title('Зависимость Продаж от отзывов критиков')

#Распределение таблиц по жанрам
genres = df.groupby('genre')['name'].count().sort_values(ascending=False)
genres

genre_sales = df.groupby('genre')['sales'].sum().sort_values(ascending=False)
genre_sales

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16, 7))
fig.autofmt_xdate()

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels1 = genres.index
sizes1 = genres.values

labels2 = genre_sales.index
sizes2 = genre_sales.values
explode = (0.25, 0.2, 0.15, 0,0,0,0,0,0,0,0,0)
ax1.set_title('Кол-во Игр по Жанрам')
ax1.pie(sizes1, labels=labels1, autopct='%1.1f%%',
        shadow=True, explode=explode,startangle=0)  
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

ax2.set_title('Кол-во Продаж по Жанрам')
ax2.pie(sizes2, labels=labels2, autopct='%1.1f%%',
        shadow=True, explode=explode,startangle=0) 
ax2.axis('equal')

plt.show()

popul_5genre_dict = {}
for region in ['na_sales', 'eu_sales', 'jp_sales']:
    popul_5genre_dict[region] = df.groupby('genre')[region].sum().sort_values(ascending=False).head(5)
popul_5genre_dict

fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(16, 6))
fig.autofmt_xdate()

i = 0
x = [ax1, ax2, ax3]
region = ['na_sales', 'eu_sales', 'jp_sales']
explode = (0.15, 0, 0, 0, 0)

for i in [0,1,2]:
    labels = popul_5genre_dict[region[i]].index
    sizes = popul_5genre_dict[region[i]].values
    ax = x[i]
    ax.set_title(f'Продажи в {region[i]}')
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode,startangle=90) 
    ax.axis('equal')  

plt.show()



