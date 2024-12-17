import requests
import streamlit as st
from dotenv import load_dotenv
import os
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

load_dotenv()
api_key = os.getenv("API_KEY")
st.set_page_config(page_title="Dashboard Clima", page_icon="⛅", layout="centered")

def get_weather_forecast(city: str) -> pd.DataFrame:
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric&lang=pt_br"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        forecast_list = []
        for item in data["list"]:
            # Convertendo a string de data para datetime
            dt = datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S")
            forecast_list.append({
                "Data e Hora": dt,
                "Temperatura (°C)": item["main"]["temp"],
                "Descrição": item["weather"][0]["description"].capitalize(),
                "Ícone": item["weather"][0]["icon"]
            })
        return pd.DataFrame(forecast_list)
    else:
        st.error("Erro: Não foi possível buscar a previsão do tempo.")
        return None

def get_icon_url(icon_code):
    return f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

st.title("☁️ Dashboard de Previsão do Clima")
cidade = st.text_input("Digite o nome da cidade:")

if cidade:
    df = get_weather_forecast(cidade)
    if df is not None:
        st.subheader("📈 Gráfico de Temperatura")
        fig = go.Figure()
        
        # Configurando o gráfico de temperatura
        fig.add_trace(go.Scatter(
            x=df["Data e Hora"],
            y=df["Temperatura (°C)"],
            mode="lines+markers+text",
            text=df["Temperatura (°C)"].apply(lambda x: f"{x:.1f}°C"),
            textposition="top center",
            textfont=dict(size=10),
            line=dict(color="#FFD700", width=2),
            marker=dict(size=6, color="white"),
            name="Temperatura"
        ))

        # Ajustes melhorados no layout
        fig.update_layout(
            xaxis=dict(
                title="Data e Hora",
                tickangle=0,
                tickformat="%H:%M\n%d/%m",
                dtick="3H",
                tickmode="linear",
                range=[df["Data e Hora"].min(), df["Data e Hora"].max()],
            ),
            yaxis=dict(
                title="Temperatura (°C)",
                range=[
                    df["Temperatura (°C)"].min() - 2,
                    df["Temperatura (°C)"].max() + 2
                ]
            ),
            template="plotly_dark",
            plot_bgcolor="#262730",
            margin=dict(l=50, r=50, t=50, b=50),
            font=dict(size=12),
            height=400
        )

        st.plotly_chart(fig, use_container_width=True)

        # Previsão Detalhada
        st.subheader("📅 Previsão para os Próximos Dias")
        cols = st.columns(5)
        
        # Corrigido o agrupamento para evitar duplicação de coluna
        df['date'] = df["Data e Hora"].dt.date
        daily_forecasts = df.groupby('date').first().reset_index()
        
        for i, (_, row) in enumerate(daily_forecasts.iterrows()):
            if i < 5:  # Limita a 5 dias
                cols[i].image(get_icon_url(row["Ícone"]), width=60)
                cols[i].markdown(f"**{row['Data e Hora'].strftime('%d/%m')}**")
                cols[i].markdown(
                    f"<span style='font-size:16px;'>{row['Temperatura (°C)']:.1f}°C</span>", 
                    unsafe_allow_html=True
                )
                cols[i].caption(row["Descrição"])