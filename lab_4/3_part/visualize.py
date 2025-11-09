import matplotlib.pyplot as plt
import pandas as pd
subjects = ['Математика', 'Физика', 'Химия', 'История', 'Обществознание']
years = [2021, 2022, 2023, 2024, 2025]


df = pd.read_csv('students.csv')
subject_avgs = {subj: [] for subj in subjects}
for year in years:
    year_data = df[df['Год поступления'] == year]
    for subj in subjects:
        scores = year_data['Балл ЦТ/ЦЭ'].apply(eval).apply(lambda x: x[subj])
        subject_avgs[subj].append(scores.mean())

for subj in subjects:
    plt.plot(years, subject_avgs[subj], label=subj)

plt.title('Динамика среднего балла ЦТ/ЦЭ')
plt.xlabel('Год')
plt.ylabel('Средний балл')
plt.legend()
plt.show()
