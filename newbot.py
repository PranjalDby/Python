import telebot 
from  telebot import TeleBot
import const
import time 

KEY = const.API_KEY
bot = telebot.TeleBot(KEY)

@bot.route('/command ?(.*)')

def example(message,cmd):
    chat_dest = message[0][0]
    user_msg = message[0]
    msg = "Pranjal Says :{}".format(user_msg)
    bot.send_message(chat_dest,msg)

example('Hello','/he')
bot.config['KEY'] = KEY
bot.poll(True)
