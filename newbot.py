import telebot 
import API_KEY
import time 

KEY = API_KEY.API_KEY
print(KEY)
bot = telebot.TeleBot(KEY,parse_mode = None)
# def message_handler(command):
#     def handle(*args,**kwargs):
#         res = ""
#         if(command[0] == '/start'):
#             res = 'Started'
#         return res
#     return handle

def sendmessage():
    bot.send_photo('@iamkingworld','bts.png','Hello  Bts')
bot.infinity_polling()

