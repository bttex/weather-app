# Dashboard de Previsão do Clima ⛅

Uma aplicação web construída com Streamlit que exibe previsões meteorológicas em tempo real, apresentando dados climáticos em um dashboard interativo e visual.

## 🌟 Funcionalidades

- Consulta de previsão do tempo para qualquer cidade
- Gráfico interativo de temperatura para os próximos dias
- Visualização diária da previsão com ícones e descrições
- Interface responsiva e amigável
- Suporte a múltiplos idiomas (português)

## 🛠️ Tecnologias Utilizadas

- Python 3.8+
- Streamlit
- Pandas
- Plotly
- OpenWeather API
- python-dotenv

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Chave de API do OpenWeather
- Conexão com internet

## 🚀 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/dashboard-clima.git
cd dashboard-clima
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Crie um arquivo `.env` na raiz do projeto e adicione sua chave API:
```
API_KEY=sua_chave_api_do_openweather
```

## 💻 Como Usar

1. Execute a aplicação:
```bash
streamlit run app.py
```

2. Abra seu navegador e acesse `http://localhost:8501`
3. Digite o nome da cidade desejada e visualize a previsão do tempo

## 📊 Recursos do Dashboard

- **Gráfico de Temperatura**: Exibe a variação de temperatura ao longo do tempo com marcadores interativos
- **Previsão Detalhada**: Mostra a previsão para os próximos 5 dias, incluindo:
  - Ícones do clima
  - Temperaturas
  - Descrições das condições meteorológicas

## 🔑 Configuração da API

Para usar esta aplicação, você precisará de uma chave API do OpenWeather:

1. Cadastre-se em [OpenWeather](https://openweathermap.org/)
2. Gere sua chave API
3. Adicione a chave ao arquivo `.env`

## 📝 Estrutura do Projeto

```
dashboard-clima/
│
├── app.py                 # Arquivo principal da aplicação
├── .env                   # Arquivo de configuração (não versionado)
├── requirements.txt       # Dependências do projeto
└── README.md             # Documentação
```

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🤝 Contribuindo

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Faça o Commit de suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Faça o Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📱 Suporte

Em caso de dúvidas ou problemas, abra uma issue no GitHub.