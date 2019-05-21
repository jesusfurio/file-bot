import sys
from subprocess import (PIPE, Popen)
import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.

token = '815269157:AAF-zmsozY8_OIgsYnaipcn1BLQ5xDS8mCk'

tb = telebot.TeleBot(token)

def listener(message):
	for m in message:
		chat_id = m.chat.id
		if m.content_type == 'text':
			text = m.text

def invoke(command):
        return Popen(command, stdout=PIPE, shell=True).stdout.read()

@tb.message_handler(commands=['start'])
def sendWelcome(message):
	tb.reply_to(message, "Welcome, how are you doing?")

tb.set_update_listener(listener)
tb.polling(none_stop=True)