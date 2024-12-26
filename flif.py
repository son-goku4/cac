import random
import telbot 
#изминения 

# замени 'TOKEN' на токен твоего бота
# этот токен ты получаешь от botfather,чтобы бот мог работать
bot = telebot.telebot("8166355541:aafbpbmtndvve3xbakm5wcfanvjffp4jipvm")

@bot.massage_handler(commands=['start'])
def send_welcome(massage):
  bot.reply_to(massage,)

@bot.massage_handler(commands=['start'])
def send_hello(massage):
  bot.reply_to(massage,)

@bot.massage_handler(commands=['start'])
def send_bye(massage):
  bot.reply_to(massage,)
