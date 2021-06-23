import telebot
from config import bot_token
from trash import create_text

class Mailer:

    def __init__(self) -> None:
        self.bot = telebot.TeleBot(bot_token)
        

    def mail(self, data : tuple) -> None:
        self.bot.send_message(data[0], create_text(data))
