import pandas as pd
from sqlalchemy import create_engine

# conexão com banco
engine = create_engine('postgresql://postgres:1234@localhost:5432/postgres')

# ler CSV
df = pd.read_csv('data/temperature_readings.csv')

# limpar dados (exemplo)
df = df.dropna()

# salvar no banco
df.to_sql('temperature_readings', engine, if_exists='replace', index=False)

print("Dados inseridos com sucesso!")