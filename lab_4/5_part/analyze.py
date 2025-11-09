import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


df = pd.read_excel('lab_4_part_5.xlsx', header=1, parse_dates=['Дата'])


df['Месяц'] = df['Дата'].dt.to_period('M')
df['Выручка'] = df['Продажи']
df['Прибыль'] = df['Продажи'] - df['Себестоимость']


pivot = df.groupby(['Месяц', 'товар'])['Выручка'].sum().unstack()
pivot.plot(marker='o', figsize=(10, 6), title='Динамика продаж по товарам')
plt.ylabel('Выручка')
plt.grid(True)
plt.tight_layout()
plt.show()


avg_sales = df.groupby('точка')['Выручка'].mean().sort_values()
avg_sales.plot(kind='barh', figsize=(8, 5), title='Средние продажи по точкам')
plt.xlabel('Средняя выручка')
plt.tight_layout()
plt.show()


for product in df['товар'].unique():
    sub = df[df['товар'] == product].groupby('Месяц')['Выручка'].sum().reset_index()
    sub['Месяц_число'] = sub['Месяц'].apply(lambda x: x.to_timestamp().toordinal())
    model = LinearRegression().fit(sub[['Месяц_число']], sub['Выручка'])
    sub['Прогноз'] = model.predict(sub[['Месяц_число']])

    plt.figure(figsize=(8, 5))
    plt.plot(sub['Месяц'].astype(str), sub['Выручка'], marker='o', label='Факт')
    plt.plot(sub['Месяц'].astype(str), sub['Прогноз'], linestyle='--', label='Прогноз')
    plt.title(f'Прогноз продаж: {product}')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()
