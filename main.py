import telebot
from telebot import types

bot = telebot.TeleBot('5153728062:AAGUQjpkkMo0dd1CRIYdDzViOydkpy_wgKI')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Hellow":
        bot.send_message(message.chat.id, 'И тебе привет', parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id} ', parse_mode='html')
    elif message.text == "photo":
        photo = open('IMG.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, 'Команда не опазнана', parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Вау! КРУТОЕ ФОТО')

# @bot.message_handler(commands=['help'])
# def website(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("Посетить ваб сайт", url="https://server-learn-qa.ru"))
#     bot.send_message(message.chat.id, 'Передите на сайт', reply_markup=markup)

bot.polling(none_stop=True)