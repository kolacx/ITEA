from bot import TGbot
from flask import Flask

TOKEN = '1053710333:AAEJtQ9h_tE6BiUD6zGVnpfXmHeaDtuH_fk'

WEBHOOK_HOST = "35.225.146.66"
PATH = "bot"
WEBHOOK_URL = f'{WEBHOOK_HOST}/{PATH}'

bot = TGbot(token=TOKEN)

app = Flask(__name__)