from turtle import update
from urllib import response

from telegram import InlineQuery, InlineQueryResult, InlineQueryResultCachedGif, User
import const as key
from telegram.ext import *
import response as R
print("Bot Started....")

def start_cmd(update,context):
    update.message.reply_text("HELLO !!! HANDSOME ❤️❤️❤️❤️❤️❤️")


def help_cmd(update,context):
    update.message.reply_text("if You are new and need Help try googling it na! right")

def handle_message(update,context):
    text = str(update.message.text).lower()
    response = R.sample_response(text)

    update.message.reply_text(response)


def error(update,context):
    print(f'update {update} caused error {context}')

def main():
    updater = Updater(key.API_KEY,use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start",start_cmd))
    dp.add_handler(CommandHandler("help",help_cmd))
    dp.add_handler(MessageHandler(Filters.text,handle_message))
    updater.idle()
    

main()


