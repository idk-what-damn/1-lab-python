import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

df = pd.read_excel('s7_data_sample_rev4_50k.xlsx', engine='openpyxl')
df.columns = df.columns.str.strip()
df['ISSUE_DATE'] = pd.to_datetime(df['ISSUE_DATE'])
df['Месяц'] = df['ISSUE_DATE'].dt.month
df['Год'] = df['ISSUE_DATE'].dt.year


print("🔹 Названия столбцов:")
print(df.columns.tolist())


print("🔹 Описательные статистики:")
print(df.describe(include='all'))


plt.figure(figsize=(10, 6))
top_routes = df.groupby(['ORIG_CITY_CODE', 'DEST_CITY_CODE']).size().sort_values(ascending=False).head(10)
top_routes.plot(kind='barh', color='skyblue')
plt.title('Топ-10 направлений по количеству билетов')
plt.xlabel('Количество')
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 5))
monthly_avg = df.groupby('Месяц')['REVENUE_AMOUNT'].mean()
sns.lineplot(x=monthly_avg.index, y=monthly_avg.values, marker='o')
plt.title('Средняя сумма продаж по месяцам')
plt.xlabel('Месяц')
plt.ylabel('Средняя сумма')
plt.grid(True)
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='PAX_TYPE', hue='PAX_TYPE', order=df['PAX_TYPE'].value_counts().index, palette='mako', legend=False)
plt.title('Распределение типов пассажиров')
plt.xlabel('Тип пассажира')
plt.ylabel('Количество')
plt.tight_layout()
plt.show()


plt.figure(figsize=(6, 6))
df['FOP_TYPE_CODE'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, cmap='Set3')
plt.title('Способы оплаты')
plt.ylabel('')
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 5))
df.groupby('SALE_TYPE')['REVENUE_AMOUNT'].sum().sort_values().plot(kind='barh', color='coral')
plt.title('Объём продаж по типу продажи')
plt.xlabel('Сумма продаж')
plt.tight_layout()
plt.show()


monthly_sales = df.groupby(['Год', 'Месяц'])['REVENUE_AMOUNT'].sum().reset_index()
X = monthly_sales[['Год', 'Месяц']]
y = monthly_sales['REVENUE_AMOUNT']

model = LinearRegression()
model.fit(X, y)
monthly_sales['Прогноз'] = model.predict(X)

plt.figure(figsize=(10, 6))
sns.lineplot(data=monthly_sales, x='Месяц', y='REVENUE_AMOUNT', hue='Год', marker='o', palette='tab10')
plt.title('Фактические продажи по месяцам и годам')
plt.xlabel('Месяц')
plt.ylabel('Сумма продаж')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.lineplot(data=monthly_sales, x='Месяц', y='Прогноз', hue='Год', linestyle='--', palette='tab10')
plt.title('Прогнозируемые продажи по месяцам и годам')
plt.xlabel('Месяц')
plt.ylabel('Прогноз суммы')
plt.tight_layout()
plt.show()
