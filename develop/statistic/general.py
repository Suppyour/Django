import pandas as pd
import matplotlib.pyplot as plt


file_path = r'C:\Users\mpors\Desktop\djangich\vacancies_2024.csv'

df = pd.read_csv(file_path)

print(df.head())

exchange_rates = {
    'USD': 100  # Пример курса за 1 USD
}

def convert_salary(row):
    if pd.notnull(row['salary_currency']) and row['salary_currency'] in exchange_rates:
        rate = exchange_rates[row['salary_currency']]
        return row['salary_to'] * rate if pd.notnull(row['salary_to']) else None
    return row['salary_to']

df['salary_rub'] = df.apply(convert_salary, axis=1)

# Динамика уровня зарплат по годам
df['published_at'] = pd.to_datetime(df['published_at'], errors='coerce')  # Преобразуем строку в дату
df['year'] = df['published_at'].dt.year
salary_dynamic = df.groupby('year')['salary_rub'].mean()

plt.figure(figsize=(10, 5))
plt.plot(salary_dynamic, marker='o')
plt.title('Динамика уровня зарплат по годам')
plt.xlabel('Год')
plt.ylabel('Средняя зарплата (руб)')
plt.grid(True)
plt.show()

# Динамика количества вакансий по годам
vacancy_dynamic = df['year'].value_counts().sort_index()

plt.figure(figsize=(10, 5))
plt.bar(vacancy_dynamic.index, vacancy_dynamic.values)
plt.title('Динамика количества вакансий по годам')
plt.xlabel('Год')
plt.ylabel('Количество вакансий')
plt.grid(True)
plt.show()

# Уровень зарплат по городам
city_salary = df.groupby('area_name')['salary_rub'].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
city_salary.plot(kind='bar')
plt.title('Уровень зарплат по городам')
plt.xlabel('Город')
plt.ylabel('Средняя зарплата (руб)')
plt.grid(True)
plt.show()

# Доля вакансий по городам
city_vacancies = df['area_name'].value_counts(normalize=True)

plt.figure(figsize=(10, 5))
city_vacancies.plot(kind='pie', autopct='%1.1f%%')
plt.title('Доля вакансий по городам')
plt.ylabel('')
plt.show()

# ТОП-20 навыков по годам
from collections import Counter

def extract_skills(skills):
    if pd.notnull(skills):
        return skills.split(',')
    return []

df['key_skills'] = daf['key_skills'].apply(extract_skills)
all_skills = df['key_skills'].sum()
top_skills = Counter(all_skills).most_common(20)

skills_df = pd.DataFrame(top_skills, columns=['skill', 'count'])

plt.figure(figsize=(10, 5))
skills_df.plot(kind='bar', x='skill', y='count')
plt.title('ТОП-20 навыков по годам')
plt.xlabel('Навык')
plt.ylabel('Количество упоминаний')
plt.grid(True)
plt.show()
