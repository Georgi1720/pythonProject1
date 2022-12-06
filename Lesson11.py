import requests
import telebot
from telebot import types
import datetime
import random

token = '5691054761:AAGSC_1IBgY8sliuy6CtQ4du0jEMEi2lQSQ'
bot = telebot.TeleBot(token)


def get_data():
    req = requests.get('https://yobit.net/api/3/ticker/btc_usd')
    response = req.json()
    sell_price = response['btc_usd']['sell']
    return f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\nСтоимость BTC: {sell_price}$"


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("Время")
    item2 = telebot.types.KeyboardButton("Кости")
    item3 = telebot.types.KeyboardButton("Таблица умножения")
    item4 = telebot.types.KeyboardButton("Курс Битка")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id,
                     'Привет, {0.first_name}!\nЯ - <u><b>{1.first_name}</b></u>, пробный бот!'.
                     format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == "Время":
        dt = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
        bot.send_message(message.chat.id, dt)
    elif message.text == 'Кости':
        r = random.randint(1, 12)
        bot.send_message(message.chat.id, r)
    elif message.text == 'Курс Битка':
        bot.send_message(message.chat.id, get_data())
    elif message.text == 'Таблица умножения':
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        item1 = telebot.types.InlineKeyboardButton('1', callback_data='1')
        item2 = telebot.types.InlineKeyboardButton('2', callback_data='2')
        item3 = telebot.types.InlineKeyboardButton('3', callback_data='3')
        item4 = telebot.types.InlineKeyboardButton('4', callback_data='4')
        item5 = telebot.types.InlineKeyboardButton('5', callback_data='5')
        item6 = telebot.types.InlineKeyboardButton('6', callback_data='6')
        item7 = telebot.types.InlineKeyboardButton('7', callback_data='7')
        item8 = telebot.types.InlineKeyboardButton('8', callback_data='8')
        item9 = telebot.types.InlineKeyboardButton('9', callback_data='9')
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)
        bot.send_message(message.chat.id, 'на какое число ? ', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == '1':
                bot.send_message(call.message.chat.id,
                                 '1 * 1 = 1\n'
                                 '1 * 2 = 2\n'
                                 '1 * 3 = 3\n'
                                 '1 * 4 = 4\n'
                                 '1 * 5 = 5\n'
                                 '1 * 6 = 6\n'
                                 '1 * 7 = 7\n'
                                 '1 * 8 = 8\n'
                                 '1 * 9 = 9\n'
                                 .format(bot.get_me()), parse_mode='html')
            elif call.data == '2':
                bot.send_message(call.message.chat.id,
                                 '2 * 1 = 2\n'
                                 '2 * 2 = 3\n'
                                 '2 * 3 = 6\n'
                                 '2 * 4 = 8\n'
                                 '2 * 5 = 10\n'
                                 '2 * 6 = 12\n'
                                 '2 * 7 = 14\n'
                                 '2 * 8 = 16\n'
                                 '2 * 9 = 18\n'
                                 .format(bot.get_me()), parse_mode='html')
            elif call.data == '3':
                bot.send_message(call.message.chat.id,
                                 '3 * 1 = 3\n'
                                 '3 * 2 = 6\n'
                                 '3 * 3 = 9\n'
                                 '3 * 4 = 12\n'
                                 '3 * 5 = 15\n'
                                 '3 * 6 = 18\n'
                                 '3 * 7 = 21\n'
                                 '3 * 8 = 24\n'
                                 '3 * 9 = 27\n'
                                 .format(bot.get_me()), parse_mode='html')
            elif call.data == '4':
                bot.send_message(call.message.chat.id,
                                 '4 * 1 = 4\n'
                                 '4 * 2 = 8\n'
                                 '4 * 3 = 12\n'
                                 '4 * 4 = 16\n'
                                 '4 * 5 = 20\n'
                                 '4 * 6 = 24\n'
                                 '4 * 7 = 28\n'
                                 '4 * 8 = 32\n'
                                 '4 * 9 = 36\n'
                                 .format(bot.get_me()), parse_mode='html')
            elif call.data == '5':
                bot.send_message(call.message.chat.id,
                                 '5 * 1 = 5\n'
                                 '5 * 2 = 10\n'
                                 '5 * 3 = 15\n'
                                 '5 * 4 = 20\n'
                                 '5 * 5 = 25\n'
                                 '5 * 6 = 30\n'
                                 '5 * 7 = 35\n'
                                 '5 * 8 = 40\n'
                                 '5 * 9 = 45\n'
                                 .format(bot.get_me()), parse_mode='html')
            elif call.data == '6':
                bot.send_message(call.message.chat.id,
                                 '6 * 1 = 6\n'
                                 '6 * 2 = 12\n'
                                 '6 * 3 = 18\n'
                                 '6 * 4 = 24\n'
                                 '6 * 5 = 30\n'
                                 '6 * 6 = 36\n'
                                 '6 * 7 = 42\n'
                                 '6 * 8 = 48\n'
                                 '6 * 9 = 54\n'
                                 .format(bot.get_me()), parse_mode='html')
            elif call.data == '7':
                bot.send_message(call.message.chat.id,
                                 '7 * 1 = 7\n'
                                 '7 * 2 = 14\n'
                                 '7 * 3 = 21\n'
                                 '7 * 4 = 28\n'
                                 '7 * 5 = 35\n'
                                 '7 * 6 = 42\n'
                                 '7 * 7 = 49\n'
                                 '7 * 8 = 56\n'
                                 '7 * 9 = 63\n'
                                 .format(bot.get_me()), parse_mode='html')
            elif call.data == '8':
                bot.send_message(call.message.chat.id,
                                 '8 * 1 = 8\n'
                                 '8 * 2 = 16\n'
                                 '8 * 3 = 24\n'
                                 '8 * 4 = 32\n'
                                 '8 * 5 = 40\n'
                                 '8 * 6 = 48\n'
                                 '8 * 7 = 56\n'
                                 '8 * 8 = 64\n'
                                 '8 * 9 = 72\n'
                                 .format(bot.get_me()), parse_mode='html')
            elif call.data == '9':
                bot.send_message(call.message.chat.id,
                                 '9 * 1 = 9\n'
                                 '9 * 2 = 18\n'
                                 '9 * 3 = 27\n'
                                 '9 * 4 = 36\n'
                                 '9 * 5 = 45\n'
                                 '9 * 6 = 54\n'
                                 '9 * 7 = 63\n'
                                 '9 * 8 = 72\n'
                                 '9 * 9 = 81\n'
                                 .format(bot.get_me()), parse_mode='html')

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Таблица', reply_markup=None)

    except Exception as e:
        print(repr(e))


bot.infinity_polling()
