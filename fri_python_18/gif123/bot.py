import telebot
import requests
import bs4
import random
from telebot import types


# сюда вставить токен
bot = telebot.TeleBot('1459823294:AAG-jdvIZgwrMh_ZmAextAMxzoOKTbGpMzI') 


@bot.message_handler(commands=['start'])
def start_message(message):
	'''Принимает команду и отвечает на неe'''
	markup = types.ReplyKeyboardMarkup()
	markup.row('привет', 'анектод')
	bot.send_message(message.chat.id, "Привет", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_text(message):
	if 'привет' in message.text.lower():
		bot.send_message(message.chat.id, 'Хай !')
	elif 'анектод' in message.text.lower():
		bot.send_message(message.chat.id, '42щш4ощ2ш323')
	elif 'пока' in message.text.lower():
		bot.send_message(message.chat.id, 'ну пока')
	elif 'гиф' in message.text.lower():
		bot.send_message(message.chat.id, 'https://media1.tenor.com/images/1226b8937eaf9c900af7e98a245f3935/tenor.gif?itemid=9922548')
	else:
		bot.send_message(message.chat.id, 'Не понимаю...')
		
@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
	'''Принимает стикер и отправляет стикер'''
	bot.send_sticker(message.chat.id, message.sticker.file_id)
	

print('Run...')
bot.polling(none_stop=False, interval=0, timeout=20)
