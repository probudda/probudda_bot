import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Безопасно получаем токен из переменной окружения
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# Делаем кнопки, которые открывают сайты внутри Telegram
keyboard = InlineKeyboardMarkup(row_width=2)
btn1 = InlineKeyboardButton("Обзор каналов в телеграм", web_app=WebAppInfo(url='https://probudda.ru/telegram'))
btn2 = InlineKeyboardButton("Карта буддийских храмов и центров", web_app=WebAppInfo(url='https://probudda.ru/map'))
btn3 = InlineKeyboardButton("Тибетский календарь", web_app=WebAppInfo(url='https://tibetanbuddhistcalendar.org/day'))
btn4 = InlineKeyboardButton("Сайт", web_app=WebAppInfo(url='https://probudda.ru/'))
keyboard.add(btn1, btn2, btn3, btn4)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я твой первый бот. Выбери кнопку (сайт откроется прямо здесь!):", reply_markup=keyboard)

print("Бот начал работу! Он теперь всегда онлайн!")
bot.infinity_polling()
