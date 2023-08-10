import tweepy
from dotenv import load_dotenv
import os

# Variables de entorno
load_dotenv()

# Llamada a la API de Twitter
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
API_KEY = os.getenv('API_KEY')
API_KEY_SECRET = os.getenv('API_KEY_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

client = tweepy.Client(BEARER_TOKEN, API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def botExec(mensaje):
    client.create_tweet(text = f'{mensaje}\n#ClimaBot')