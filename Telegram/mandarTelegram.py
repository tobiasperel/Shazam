import telegram
from telegram.ext import *
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from Telegram.keysTelegram import *

bot = telegram.Bot(token=token)

def send_message(text= "Se corto el programa",chat_id = chat_id):
    bot.send_message(chat_id, text)

#send_message(chat_id,'hola chino')
