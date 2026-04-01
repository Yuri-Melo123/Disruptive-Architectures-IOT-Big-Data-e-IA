import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg://postgres:1234@localhost:5432/postgres"
)

def load_data(view):
    return pd.read_sql(f"SELECT * FROM {view}", engine)

st.title('Dashboard IoT')

# gráfico 1
df1 = load_data('avg_temp_por_dispositivo')
st.header('Média por dispositivo')
st.plotly_chart(px.bar(df1, x='device_id', y='avg_temp'))

# gráfico 2
df2 = load_data('leituras_por_hora')
st.header('Leituras por hora')
st.plotly_chart(px.line(df2, x='hora', y='contagem'))

# gráfico 3
df3 = load_data('temp_max_min_por_dia')
st.header('Temperatura por dia')
st.plotly_chart(px.line(df3, x='data', y=['temp_max', 'temp_min']))