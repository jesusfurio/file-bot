import sys
from subprocess import (PIPE, Popen)
import telebot 
from telebot import types 
import time 

token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

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
