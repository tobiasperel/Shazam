import telegram
from telegram.ext import *
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from Telegram.keysTelegram import *

bot = telegram.Bot(token=token)

def send_message(text= "Se corto el programa",chat_id = chat_id):
    try:
        bot.send_message(chat_id, text)
    except:
        send_message()

#send_message(chat_id,'hola chino')
