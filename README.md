
# Weather-app

A função getweather usa a API do OpenWeatherMap para recuperar dados climáticos para uma cidade dada.

Parâmetros
| Nome | Tipo | Descrição |
|------|------|------------|
| `cidade` | `str` | O nome da cidade para a qual recuperar dados climáticos. |

Retorna
Uma lista contendo os seguintes dados climáticos para a cidade especificada:

Nome da cidade
País
Temperatura em graus Celsius
Condição climática
Descrição climática
Velocidade do vento
Direção do vento
Humidade


Exceções
| Exceção | Descrição |
|---------|-----------|
| `ValueError` | Se a cidade de entrada não for um nome de cidade válido. |

# Como usar
Você pode chamar a função getweather passando o nome da cidade como um parâmetro. A função retornará uma lista com os dados climáticos para a cidade especificada.

``` bash
>>> dados_climaticos = getweather('Sao Paulo')
>>> print(dados_climaticos)
['Sao Paulo', 'Brasil', 27.15, 'Céu', 'Nublado', 12.1, 220, 75]
```

Se a cidade não for encontrada, a função getweather lançará uma exceção ValueError.

``` bash
>>> dados_climaticos = getweather('Paris')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "weather.py", line 30, in getweather
    raise ValueError(f"Não foi possível encontrar {cidade}. Por favor, verifique o nome da cidade e tente novamente.")
ValueError: Não foi possível encontrar Paris. Por favor, verifique o nome da cidade e tente novamente.
```
## Instalação

Instale a biblioteca requests

```bash
  pip install requests
```
Execute o arquivo python.

Lembre-se de ter uma API Key do openweather
