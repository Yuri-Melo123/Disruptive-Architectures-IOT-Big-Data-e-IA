import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg://postgres:1234@localhost:5432/postgres")

st.title('Dashboard IoT - Temperaturas')

try:
    df1 = pd.read_sql("SELECT * FROM avg_temp_por_dispositivo", engine)
    st.header('Média de temperatura por dispositivo')
    st.plotly_chart(px.bar(df1, x='room_id', y='avg_temp'))
except Exception as e:
    st.error(f"Erro: {e}")

try:
    df2 = pd.read_sql("SELECT * FROM leituras_por_hora", engine)
    st.header('Leituras por hora do dia')
    st.plotly_chart(px.line(df2, x='hora', y='contagem'))
except Exception as e:
    st.error(f"Erro: {e}")

try:
    df3 = pd.read_sql("SELECT * FROM temp_max_min_por_dia", engine)
    st.header('Temperaturas máximas e mínimas por dia')
    st.plotly_chart(px.line(df3, x='dia', y=['temp_max', 'temp_min']))
except Exception as e:
    st.error(f"Erro: {e}")