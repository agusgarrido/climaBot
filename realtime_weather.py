import requests
from dotenv import load_dotenv
import os
from bot import *

# Variables de entorno
load_dotenv()

# Llamada a la API
API_KEY_WEATHER = os.getenv('API_KEY_WEATHER')

url = f"https://api.tomorrow.io/v4/weather/realtime?location=buenos%20aires&apikey={API_KEY_WEATHER}"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers).json()

def realtime(response):
    response = response
    # Localizacion
    localizacion = response['location']['name']

    # Tiempo real
    values = response['data']['values']
    temperatura = values['temperature']
    sensacion_termica = values['temperatureApparent']
    humedad = values['humidity']
    prob_precipitacion = values['precipitationProbability']

    return f'{localizacion}\nTemperatura: {temperatura:.0f}°C || Sensación Térmica: {sensacion_termica:.0f}°C\nHumedad: {humedad}% || Prob. Precipitación: {prob_precipitacion}%'

# Ejecución
mensaje = realtime(response)
botExec(mensaje)