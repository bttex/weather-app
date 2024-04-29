import requests


api_key = 'a81dfdae05114379ed408e7540f2f4b6'




url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

def getweather(cidade: str) -> list:
    """
    Esta função usa a API do OpenWeatherMap para recuperar dados climáticos para uma cidade dada.

    Args:
        cidade (str): O nome da cidade para a qual recuperar dados climáticos.

    Returns:
        list: Uma lista contendo os seguintes dados climáticos para a cidade especificada:
            - Nome da cidade
            - País
            - Temperatura em graus Celsius
            - Condição climática
            - Descrição climática
            - Velocidade do vento
            - Direção do vento
            - Humidade

    Raises:
        ValueError: Se a cidade de entrada não for um nome de cidade válido.

    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}"

    resultado = requests.get(url)

    if resultado:
        json = resultado.json()
        cidade = json["name"]
        país = json["sys"]["country"]
        temperatura_kelvin = json["main"]["temp"]
        temperatura_celsius = temperatura_kelvin - 273.15
        temperatura_celsius = round(temperatura_celsius, 2)
        clima1 = json["weather"][0]["main"]
        descricao = json["weather"][0]["description"].capitalize()
        vento = json["wind"]["speed"]
        direção_do_vento = json["wind"]["deg"]
        humidade = json["main"]["humidity"]
        final = [cidade, país, temperatura_celsius, clima1, descricao, vento, direção_do_vento, humidade]
        return final
    else:
        raise ValueError(f"Não foi possível encontrar {cidade}. Por favor, verifique o nome da cidade e tente novamente.")

def search(nome_cidade):
		data = getweather(nome_cidade)
		if data:
			print(f"{'-'*35}\nCidade: {data[0]}, {data[1]}\nTemperatura: {data[2]}\nCondições Climáticas: {data[3]}\nDescrição: {data[4]}\n\nDetalhes Adicionais:\n\tVelocidade do Vento: {data[5]}km/h\n\tDireção do vento {data[6]} Graus\nHumidade: {data[7]}%\n{'-'*35}")
		else:
			return 'Error', f"Cannot find {city}",'\n'+"Please enter a real city's name... not an imaginary ones' xd"

cidade = input(">>> Digite o nome da cidade:\n>>> ")
search(cidade)