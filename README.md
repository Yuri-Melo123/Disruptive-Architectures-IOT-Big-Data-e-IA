# Pipeline de Dados com IoT, Docker e PostgreSQL

## Descrição do Projeto

Este projeto tem como objetivo desenvolver um pipeline de dados completo utilizando dados de dispositivos IoT (sensores de temperatura). O sistema realiza a ingestão, processamento, armazenamento e visualização dos dados.

## Tecnologias Utilizadas

* Python
* Pandas
* PostgreSQL
* Docker
* SQLAlchemy
* Streamlit
* Plotly

## Estrutura do Projeto

```
Disruptive-Architectures-IOT-Big-Data-e-IA/
 ├── data/
 ├── src/
 │    ├── pipeline.py
 │    ├── dashboard.py
 ├── sql/
 │    ├── views.sql
 ├── README.md
 ├── requirements.txt
```

## Como Executar o Projeto

### 1. Clonar o repositório

```
git clone https://github.com/Yuri-Melo123/Disruptive-Architectures-IOT-Big-Data-e-IA.git
cd Disruptive-Architectures-IOT-Big-Data-e-IA
```

### 2. Instalar dependências

```
pip install -r requirements.txt
```

### 3. Subir o PostgreSQL com Docker

```
docker run --name postgres-iot -e POSTGRES_PASSWORD=1234 -p 5432:5432 -d postgres
```

### 4. Executar o pipeline de dados

```
python src/pipeline.py
```

### 5. Criar as views no banco

Execute o arquivo:

```
sql/views.sql
```

### 6. Rodar o dashboard

```
streamlit run src/dashboard.py
```

## Views Criadas

### 🔹 Média de temperatura por dispositivo

Permite identificar quais dispositivos apresentam maiores temperaturas médias.

### 🔹 Leituras por hora

Mostra o volume de dados coletados ao longo do dia.

### 🔹 Temperaturas máximas e mínimas por dia

Permite analisar variações térmicas diárias.

## Insights Obtidos

* Identificação de dispositivos com comportamento anômalo
* Horários com maior atividade de sensores
* Variação térmica ao longo do tempo

## Dataset

Disponível em:
https://www.kaggle.com/datasets/atulanandjha/temperature-readings-iot-devices

## Comandos Git Utilizados

```
git init
git add .
git commit -m "Projeto inicial"
git push
```

## DesenvolLink para a explicação no Youtube

https://youtu.be/

Desenvolvido por Yuri de Oliveira Melo
