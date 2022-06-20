import telegram
from telegram.ext import *
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from Telegram.keysTelegram import *

bot = telegram.Bot(token=token)

def send_message(chat_id = chat_id, text= "Se corto el programa"):
    bot.send_message(chat_id, text)

#send_message(chat_id,'hola chino')
