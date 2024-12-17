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
        
        # Área preenchida abaixo da linha
        fig.add_trace(go.Scatter(
            x=df["Data e Hora"],
            y=df["Temperatura (°C)"],
            fill='tozeroy',
            fillcolor='rgba(255, 183, 77, 0.2)',
            line=dict(color='rgb(255, 183, 77)', width=2),
            mode='lines',
            showlegend=False
        ))
        
        # Linha principal e pontos
        fig.add_trace(go.Scatter(
            x=df["Data e Hora"],
            y=df["Temperatura (°C)"],
            mode="lines+markers+text",
            text=df["Temperatura (°C)"].apply(lambda x: f"{int(x)}°"),
            textposition="top center",
            textfont=dict(
                size=13,
                color='white'
            ),
            line=dict(color='rgb(255, 183, 77)', width=2),
            marker=dict(
                size=1,
                color='rgb(255, 183, 77)',
            ),
            showlegend=False
        ))

        # Layout atualizado para parecer com o Google Clima
        fig.update_layout(
            plot_bgcolor='rgb(32, 33, 36)',  # Cor de fundo escura
            paper_bgcolor='rgb(32, 33, 36)',
            margin=dict(l=20, r=20, t=10, b=20),
            height=250,  # Altura reduzida
            xaxis=dict(
                showgrid=False,
                showline=False,
                tickformat="%H:%M",  # Apenas hora
                tickangle=0,
                dtick="3H",
                tickmode="linear",
                tickfont=dict(size=11, color='rgb(154, 160, 166)'),
                zeroline=False,
            ),
            yaxis=dict(
                showgrid=False,
                showline=False,
                zeroline=False,
                tickfont=dict(size=11, color='rgb(154, 160, 166)'),
                range=[
                    df["Temperatura (°C)"].min() - 5,
                    df["Temperatura (°C)"].max() + 5
                ]
            )
        )

        st.plotly_chart(fig, use_container_width=True)

        # Previsão Detalhada
        st.subheader("📅 Previsão para os Próximos Dias")
        cols = st.columns(5)
        
        df['date'] = df["Data e Hora"].dt.date
        daily_forecasts = df.groupby('date').agg({
            'Data e Hora': 'first',
            'Temperatura (°C)': lambda x: [x.max(), x.min()],
            'Descrição': 'first',
            'Ícone': 'first'
        }).reset_index()
        
        for i, row in daily_forecasts.iterrows():
            if i < 5:
                temp_max, temp_min = row['Temperatura (°C)']
                cols[i].image(get_icon_url(row["Ícone"]), width=60)
                cols[i].markdown(f"**{row['Data e Hora'].strftime('%d/%m')}**")
                cols[i].markdown(
                    f"<span style='font-size:16px;'>{int(temp_max)}° {int(temp_min)}°</span>", 
                    unsafe_allow_html=True
                )
                cols[i].caption(row["Descrição"])