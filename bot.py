import telebot
from config import token


bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    with open('video_mem/bober.gif', 'rb') as f: 
        bot.send_video(message.chat.id, f, caption='Сортировать мусор нужно правильно. Выбери тему которая тебя интересует: /trash (о мусоре), /glass (стекло), /plastic (пластик), /metal (металл), /paper (бумага).👍')

@bot.message_handler(commands=['trash'])
def send_bye(message):
    with open('video_mem/bober.gif', 'rb') as f:  
        bot.send_video(message.chat.id, f, caption='Поговорим о мусоре в целом. Мусор бывает переробатываемым и непереробатываемым. Непереробатываемый мусор нельзя выбрасывать вместе с переробатываемым. Переробатываемый мусор нужно мыть если он грязный (работает со стеклом, пластиком и металлом). Мусор так же можно использовать в искустве.✔')

@bot.message_handler(commands=['glass'])
def send_bye(message):
    with open('video_mem/smile.gif', 'rb') as f:  
        bot.send_video(message.chat.id, f, caption='Перед выбрасыванием стекло нужно сложить в коробку, чтобы животные случайно не поранились.😉')

@bot.message_handler(commands=['plastic'])
def send_bye(message):
    with open('video_mem/chips.gif', 'rb') as f:  
        bot.send_video(message.chat.id, f, caption='Пластик, если он  грязный, перед выбрасыванием нужно помыть.👌')

@bot.message_handler(commands=['metal'])
def send_bye(message):
    with open('video_mem/skeleton.gif', 'rb') as f:  
        bot.send_video(message.chat.id, f, caption='Большинство металов можно сдать в металоприемник, так еще и заработать на этом!😎') 

@bot.message_handler(commands=['paper'])
def send_bye(message):
    with open('images/plane.jpg', 'rb') as f:  
        bot.send_photo(message.chat.id, f, caption='Из бумаги и картона можно делать поделки и оригами. Из картона ты можешь сделать домик для своего питомца, а из бумаги - бумажный самолетик. Больше идей ты можешь найти в Интернете!🎁')

bot.infinity_polling()