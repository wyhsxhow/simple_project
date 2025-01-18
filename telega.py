import time
import telebot
from func_db import add_user, create_table, log_message

TOKEN = ''
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    add_user(message.from_user.id, message.from_user.username)
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler(func=lambda message:True)
def echo_all(message):
    log_message(message.from_user.id, message.text)
    bot.send_message(message.chat.id, 'Ваше сообщение сохранено в базе данных!')

while True:
    try:
        create_table()
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(15)
