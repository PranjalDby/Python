from datetime import datetime
from tkinter.messagebox import RETRY

def sample_response(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello" ,"hi"):
        return "Hey! How's is Going"

    if(user_message in ("who are you","who are you?")):
        return " I am MARINA 😊 A USER _FRIENDLY BOT"

    if user_message in ("time","time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y,%H:%M:%S")

        return date_time
    if user_message in ["😊","😂","🤣","❤️"]:
        mess = "💕💕💕💕💕💕"
    return "I don't Understand"




    