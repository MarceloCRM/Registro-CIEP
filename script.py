import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'login.settings')

django.setup()
import pandas as pd
from registros.models import Registros

df = pd.read_csv('c:/Users/Marcelo/Downloads/RegistroAlunos1.csv', delimiter=';', encoding='ISO-8859-1')

df['Data de nascimento'] = pd.to_datetime(df['Data de nascimento'], format='%d/%m/%Y', errors='coerce')

df = df.dropna(subset=['Data de nascimento'])
df['Data de nascimento'] = df['Data de nascimento'].dt.strftime('%Y-%m-%d')

for index, row in df.iterrows():
    objeto = Registros(
        nome=row['Nome completo'],
        nome_mae=row['Nome da mae'],
        data_nascimento=row['Data de nascimento'],
        numero_caixa=row['Numero da caixa']
    )
    objeto.save()
