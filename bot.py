import telebot
import ollama

MODEL = 'phi3'

token='7117200365:AAFkFjzxT6k_Fd7ZvuhjpcpaLidsl42MpvA'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет')

@bot.message_handler(content_types='text')
def message_reply(message):
    messagee = {'role':'user', 'content': message.text}
    response = ollama.chat(model=MODEL, messages=[messagee])
    bot.send_message(message.chat.id, response['message']['content'])
    
bot.infinity_polling()
