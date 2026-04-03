import pandas as pd
from sqlalchemy import create_engine, text
import os

engine = create_engine("postgresql+psycopg://postgres:1234@localhost:5432/postgres")

def setup():
    csv_path = os.path.join(os.path.dirname(__file__), '../data/IOT-temp.csv')
    print(f"Lendo {csv_path}")
    df = pd.read_csv(csv_path, encoding='latin1')
    print("Colunas originais:", df.columns.tolist())

    # Cria novas colunas a partir das originais
    df['room_id'] = df['room_id/id']
    df['temperature'] = df['temp']
    df['status'] = df['out/in']
    
    # Mantém APENAS as colunas desejadas (remove 'id' porque não é numérico e não é necessário)
    df = df[['room_id', 'noted_date', 'temperature', 'status']]
    
    # Converte data
    df['noted_date'] = pd.to_datetime(df['noted_date'], dayfirst=True, errors='coerce')
    df = df.dropna(subset=['noted_date', 'temperature'])
    
    # Recria a tabela do zero (sem a coluna 'id')
    with engine.connect() as conn:
        conn.execute(text("DROP TABLE IF EXISTS temperature_readings CASCADE;"))
        conn.execute(text("""
            CREATE TABLE temperature_readings (
                room_id VARCHAR(100),
                noted_date TIMESTAMP,
                temperature FLOAT,
                status VARCHAR(10)
            );
        """))
        conn.commit()
    
    # Insere os dados
    df.to_sql('temperature_readings', engine, if_exists='append', index=False)
    print(f"Inseridos {len(df)} registros.")
    
    # Cria as views
    with engine.connect() as conn:
        conn.execute(text("DROP VIEW IF EXISTS avg_temp_por_dispositivo CASCADE;"))
        conn.execute(text("""
            CREATE VIEW avg_temp_por_dispositivo AS
            SELECT room_id, AVG(temperature) as avg_temp
            FROM temperature_readings
            GROUP BY room_id;
        """))
        conn.execute(text("DROP VIEW IF EXISTS leituras_por_hora CASCADE;"))
        conn.execute(text("""
            CREATE VIEW leituras_por_hora AS
            SELECT EXTRACT(HOUR FROM noted_date) as hora, COUNT(*) as contagem
            FROM temperature_readings
            GROUP BY hora
            ORDER BY hora;
        """))
        conn.execute(text("DROP VIEW IF EXISTS temp_max_min_por_dia CASCADE;"))
        conn.execute(text("""
            CREATE VIEW temp_max_min_por_dia AS
            SELECT DATE(noted_date) as dia,
                   MAX(temperature) as temp_max,
                   MIN(temperature) as temp_min
            FROM temperature_readings
            GROUP BY dia
            ORDER BY dia;
        """))
        conn.commit()
    print("Views criadas com sucesso.")

if __name__ == "__main__":
    setup()