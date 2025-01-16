import telebot
import os
import random
import requests
TOKEN = '8166355541:AAFbPBMtNdVVE3xBAKm5wcfanVjFp4JlpvM'
bot = telebot.TeleBot(TOKEN)
def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.message_handler(commands=['duck'])
def duck(message):
    '''По команде duck вызывает функцию get_duck_image_url и отправляет URL картинку '''
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)
@bot.message_handler(commands=['mem'])
def mem(message):
    '''Отправляет случайную картинку из папки images'''
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        bot.send_photo(message.chat.id, f)
bot.polling()
