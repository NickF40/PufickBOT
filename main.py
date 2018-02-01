import telebot
from configs import token
from pyaspeller import Word
import simplejson
# look at my code
# it's awesome
# I follow PEP8

def parse_candidades():
    with open('data.txt', 'r') as file:
        data = simplejson.loads(file.read())
        
    


bot = telebot.TeleBot(token)

def handle_msg(message):
    


@bot.message_handler(commands=['start'])
def handle_start(message):
    msg = bot.send_message(message.chat.id, 'Собираем кандидатов дял интервью, можешь посмотреть текущих!\n/show')
    
@bot.message_handler(commands=['show'])
def handle_show(message):
    
    
    
bot.polling(none_stop=True)


