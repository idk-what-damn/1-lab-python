from faker import Faker
import pandas as pd
import random

fake = Faker('ru_RU')
years = [2021, 2022, 2023, 2024, 2025]
forms = ['дневная', 'заочная', 'вечерняя']
specialties = ['Информатика', 'Экономика', 'Физика', 'Математика', 'Биология']
subjects = ['Математика', 'Физика', 'Химия', 'История', 'Обществознание']

data = []
for _ in range(100):
    year = random.choice(years)
    form = random.choice(forms)
    subject_scores = {subj: random.randint(30, 100) for subj in subjects}
    avg_certificate = round(random.uniform(5.0, 10.0), 2)
    total_score = sum(subject_scores.values()) + avg_certificate * 10
    data.append({
        'ФИО': fake.name(),
        'Год поступления': year,
        'Форма обучения': form,
        'Балл ЦТ/ЦЭ': subject_scores,
        'Средний балл аттестата': avg_certificate,
        'Общий балл': total_score,
        'Специальность': random.choice(specialties),
        'Адрес': fake.address(),
        'Телефон': fake.phone_number()
    })

df = pd.DataFrame(data)
df.to_csv('students.csv', index=False)
