#!/usr/bin/python3

import os
import telebot
import logging

TOKEN = '1486281145:AAFLUFbwX8Qt4Uf23fmA47BUm88hZh5uJ8M'
#TOKEN = os.environ['TELETOKEN']

bot = telebot.TeleBot(TOKEN)
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
    Hi there, I am EchoBot.\
    And you are a cock!\
    I am here to echo your kind words back to you.\
    Just say anything nice and I'll say the exact same thing to you!\
    """)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)
