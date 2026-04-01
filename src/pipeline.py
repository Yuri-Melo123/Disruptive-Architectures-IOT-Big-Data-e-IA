import pandas as pd
from sqlalchemy import create_engine

# conexão com banco
engine = create_engine(
    "postgresql+psycopg://postgres:1234@localhost:5432/postgres"
)

# definir colunas
df.columns = [
    'id',
    'room_id',
    'noted_date',
    'temperature',
    'status'
]

# converter data
df['noted_date'] = pd.to_datetime(df['noted_date'])

# ler CSV
df = pd.read_csv('data/IOT-temp.csv', encoding='latin1')

# limpar dados (exemplo)
df = df.dropna()

# salvar no banco
df.to_sql('temperature_readings', engine, if_exists='replace', index=False)

print("Dados inseridos com sucesso!")