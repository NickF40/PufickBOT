import telebot
from configs import token
from pyaspeller import Word
# look at my code
# it's awesome
# I follow PEP8




bot = telebot.TeleBot(token)



def parsed_data():
    file_ = open('data.txt', 'r')
    data = file_.read()
    data = data.split(';')
    file_.close()
    return data


def handle_msg(message):
    if len(message.text) < 1000 or len(message.text) <10 or len(message.text.split()) == 1:
        text = ""
        for s in message.text.split():
            if len(s) > 20:
                continue
            w = Word(s)
            if w.spellsafe:
                text = " ".join([text, w.spellsafe])
            elif w.correct:
                text = " ".join([text, s])
            else:
                continue
        print(text)
        text.replace(';', '.')
        if not text:
            msg = bot.send_message(message.chat.id, 'Не шали!\nПопробуй ещё раз!')
            bot.register_next_step_handler(msg, handle_msg)
        if text not in parsed_data():
            file_ = open('data.txt', 'a')
            file_.write(text+';')
            msg = bot.send_message(message.chat.id, 'Хороший вопрос!\nМы его немного обработали для удобства..\n%s\nПродолжай!' % text)
            bot.register_next_step_handler(msg, handle_msg)
        else:
            msg = bot.send_message(message.chat.id, 'Повторяетесь!\nПопробуй ещё раз!')
            bot.register_next_step_handler(msg, handle_msg)
    else:
        msg = bot.send_message(message.chat.id, 'Не шали!\nПопробуй ещё раз!')
        bot.register_next_step_handler(msg, handle_msg)



@bot.message_handler(commands=['start'])
def handle_start(message):
    msg = bot.send_message(message.chat.id, 'Мы готовим интервью для Тимофека!\n'
                                            'Помоги нам составить для него список вопросов - отправь вопрос,'
                                            ' который бы ты задал Тимофеку, и, если он будет адекватный,'
                                            ' мы обязательно его зададим!')
    bot.register_next_step_handler(msg, handle_msg)


bot.polling(none_stop=True)


