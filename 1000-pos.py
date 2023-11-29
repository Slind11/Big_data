import pandas as pd
from faker import Faker
import random
import matplotlib.pyplot as plt
import seaborn as sns

# Создание случайных данных с помощью библиотеки Faker
fake = Faker("ru_RU")

def generate_snils():
    # Генерация СНИЛС
    snils = ''.join([str(random.randint(0, 9)) for _ in range(9)])
    return f"{snils[:3]}-{snils[3:6]}-{snils[6:9]} {random.randint(1, 99):02}"

def generate_inn():
    # Генерация ИНН
    inn = ''.join([str(random.randint(0, 9)) for _ in range(10)])
    return f"{inn[:4]}-{inn[4:]}"

data = {
    'ФИО': [fake.name() for _ in range(1000)],
    'Возраст': [random.randint(18, 65) for _ in range(1000)],
    'Место жительства': [fake.city() for _ in range(1000)],
    'Семейное положение': [random.choice(['Женат/Замужем', 'Холост/Не замужем']) for _ in range(1000)],
    'Cнилc': [generate_snils() for _ in range(1000)],
    'ИНН': [generate_inn() for _ in range(1000)]
}

df = pd.DataFrame(data)

df['Категория возраста'] = pd.cut(df['Возраст'], bins=[18, 30, 40, 50, 60, 70], labels=['18-30', '31-40', '41-50', '51-60', '61-70'])

print("Статистика по числовым данным:")
print(df['Возраст'].describe())
print("\nРаспределение семейного положения:")
print(df['Семейное положение'].value_counts())

# Визуализация данных
plt.figure(figsize=(12, 6))

# Гистограмма распределения возраста
plt.subplot(1, 2, 1)
sns.histplot(df['Возраст'], bins=20, kde=True)
plt.title('Распределение возраста')

# Круговая диаграмма семейного положения
plt.subplot(1, 2, 2)
df['Семейное положение'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Семейное положение')

plt.tight_layout()
plt.show()
