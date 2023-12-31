import requests
from datetime import datetime
from babel.dates import format_date
from bot import *
from dotenv import load_dotenv
import os

# Variables de entorno
load_dotenv()

# Llamada a la API
API_KEY_WEATHER = os.getenv('API_KEY_WEATHER')

url = f"https://api.tomorrow.io/v4/weather/forecast?location=buenos%20aires&apikey={API_KEY_WEATHER}"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers).json()

# Obtener día
def obtenerNombre(fecha):
    fecha = datetime.strptime(fecha, "%Y-%m-%dT%H:%M:%SZ")
    locale = 'es'
    return format_date(fecha, 'EEEE', locale=locale).upper()

# Pronóstico semanal
def forecast(response):
    dias = response['timelines']['daily']
    pronostico = ''
    for dia in dias[1:4]:
        values = dia['values']
        nombre_dia = obtenerNombre(dia['time']).upper() 
        temperatura_min = values['temperatureMin']
        temperatura_max = values['temperatureMax']
        prob_precipitacion = values['precipitationProbabilityAvg']
        pronostico += f'{nombre_dia}\nMin: {temperatura_min:.0f}°C - Max {temperatura_max:.0f}°C || Prob. Precipitación: {prob_precipitacion}%\n'
    return pronostico

# Ejecución
pronostico = forecast(response)
mensaje = f'/ PRONÓSTICO EXTENDIDO /\n{pronostico}'
botExec(mensaje)