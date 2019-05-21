import sys
from subprocess import (PIPE, Popen)
import telebot 
from telebot import types 
import time 

token = 'XXXXXXXXXXXXXXXXXXXX'

bot = telebot.TeleBot(token)

def listener(message):
	for m in message:
		chat_id = m.chat.id
		if m.content_type == 'text':
			text = m.text

bot.set_update_listener(listener)

def invoke(command):
        return Popen(command, stdout=PIPE, shell=False, encoding='utf-8').stdout.read()

@bot.message_handler(commands=['start'])
def sendWelcome(message):
	bot.reply_to(message, """Welcome. What are you doing?
    /list --> Show a file list
    /get --> Use /get name_file to download file
    """)

@bot.message_handler(commands=['list'])
def sendList(m):
    chat_id = m.chat.id
    file_list = "cat /directory/prueba.txt"
    result = invoke(file_list)
    bot.send_message(chat_id, result)

@bot.message_handler(commands=['get'])
def getFile(m):
    import requests
    chat_id = m.chat.id
    msg = m.text[4:]
    search_file = "grep -i {} /directorys/prueba.txt".format(msg)
    execute_search = invoke(search_file)
    if (len(execute_search.split('\n'))) > 2 or (len(execute_search.split('\n'))) < 2:
        bot.send_message(chat_id, "More than one result, please repeat search :")
    else:
        result = "/directory/files/{}".format(execute_search)
        result = result.rstrip('\n')
        print(result)
        files = open(result,'rb')
        bot.send_document(chat_id, files)

bot.polling(none_stop=True)

while True:

    try:

        bot.polling(none_stop=True)

    # ConnectionError and ReadTimeout because of possible timout of the requests library

    # TypeError for moviepy errors

    # maybe there are others, therefore Exception

    except Exception as e:

        print(e)

        time.sleep(15)