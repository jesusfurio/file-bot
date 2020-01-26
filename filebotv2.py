import telebot
import os 
from telebot import types 

token = 'token'

bot = telebot.TeleBot(token)

def listener(message):
	for m in message:
		chat_id = m.chat.id
		if m.content_type == 'text':
			text = m.text

bot.set_update_listener(listener)

folder = "/path_with_files/"

@bot.message_handler(commands=['start'])
def sendWelcome(message):
	bot.reply_to(message, """Welcome. What are you doing?
    /list --> Show a file list
    /get --> Use /get name_file to download file
    """)

@bot.message_handler(commands=['list'])
def sendList(m):
    chat_id = m.chat.id
    
    for i in os.listdir(folder):
        f = os.path.join(i)
        bot.send_message(chat_id, f)

@bot.message_handler(commands=['get'])
def getFile(m):
    chat_id = m.chat.id
    msg = m.text[5:]
    result = folder + msg
    
    while True:
        try:
            files = open(result,'rb')
            bot.send_document(chat_id, files)
            break
        except FileNotFoundError:
            bot.send_message(chat_id, "Fichero no encontrado. Por favor, asegúrate de que el nombre esté bien escrito")
            break
        except IsADirectoryError:
            bot.send_message(chat_id, "Debes especificar el nombre de un fichero.")
            break

bot.polling(none_stop=True)

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(15)
