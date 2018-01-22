from telebot import TeleBot
from telebot import types as telebot
from sqlite import *
from tools import collect_trash
from time import asctime
from sqlite import *


class Function:
    def __init__(self, f, type_, **kwargs):
        pass


class Bot:
    def __init__(self, token):
        self.token = token
        self.bot = TeleBot(token)
        self.init_time = asctime()
        self.funcs = []

    def message_handler(self, func, dec):
        # @dec
        # func
        pass

    def init_handlers(self):
        self.bot.message_handlers = []
        self.bot.edited_message_handlers = []
        self.bot.channel_post_handlers = []
        self.bot.edited_channel_post_handlers = []
        self.bot.inline_handlers = []
        self.bot.chosen_inline_handlers = []
        self.bot.callback_query_handlers = []
        self.bot.shipping_query_handlers = []
        self.bot.pre_checkout_query_handlers = []
        for f in self.funcs:
            self.message_handler(f.function, f.dec(f.kwargs))


class Engine:
    def __init__(self, token):
        self.sqlite_conn = authorize()
        self.bot = Bot(token)

    def start(self):
        self.bot.init_handlers()
        self.bot.polling(none_stop=True)

    def stop(self):
        terminate(self.sqlite_conn)
        self.bot.stop_polling()
        collect_trash()
