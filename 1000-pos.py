import pandas as pd
from faker import Faker
import random

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

print(df.head(20))
