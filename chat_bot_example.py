import telebot
from telebot import apihelper
import time

TOKEN = '2072721110:AAEBClndY1y8B8zG9IUELYotHy_AB3a4Djc'

proxies = {
    'http': 'https://173.245.49.19:80',
}

apihelper.proxy = proxies
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['start'])
def commnad_start_function(message):
    bot.reply_to(message, 'Рад Вас приветствовать!')

@bot.message_handler(commands = ['admin'])
def admin(message):
    print(message)
    bot.reply_to(message, 'Хозяин, я рад тебя приветствовать!')

@bot.message_handler(content_types = ['text'])
def recieve_text(message):
    text = message.text
    bot.reply_to(message, f'Вы сказали: {text}')

bot.polling()