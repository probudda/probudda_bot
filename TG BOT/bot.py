import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# ВСТАВЬ СЮДА СВОЙ ТОКЕН! Скопируй его из @BotFather
import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Безопасно получаем токен из переменной окружения
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# Делаем кнопки, которые открывают сайты внутри Telegram
keyboard = InlineKeyboardMarkup(row_width=2)
btn1 = InlineKeyboardButton("YouTube", web_app=WebAppInfo(url='https://youtube.com'))
btn2 = InlineKeyboardButton("Google", web_app=WebAppInfo(url='https://google.com'))
btn3 = InlineKeyboardButton("Википедия", web_app=WebAppInfo(url='https://wikipedia.org'))
btn4 = InlineKeyboardButton("GitHub", web_app=WebAppInfo(url='https://github.com'))
btn5 = InlineKeyboardButton("Переводчик", web_app=WebAppInfo(url='https://translate.google.com'))
btn6 = InlineKeyboardButton("Карты", web_app=WebAppInfo(url='https://yandex.ru/maps'))
keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я твой первый бот. Выбери кнопку (сайт откроется прямо здесь!):", reply_markup=keyboard)

print("Бот начал работу! Он теперь всегда онлайн!")
bot.infinity_polling()

# Делаем кнопки, которые открывают сайты внутри Telegram
keyboard = InlineKeyboardMarkup(row_width=2)

# Обрати внимание: теперь используется web_app=WebAppInfo(url="ССЫЛКА")
btn1 = InlineKeyboardButton("YouTube", web_app=WebAppInfo(url='https://youtube.com'))
btn2 = InlineKeyboardButton("Google", web_app=WebAppInfo(url='https://google.com'))
btn3 = InlineKeyboardButton("Википедия", web_app=WebAppInfo(url='https://wikipedia.org'))
btn4 = InlineKeyboardButton("GitHub", web_app=WebAppInfo(url='https://github.com'))
btn5 = InlineKeyboardButton("Переводчик", web_app=WebAppInfo(url='https://translate.google.com'))
btn6 = InlineKeyboardButton("Карты", web_app=WebAppInfo(url='https://yandex.ru/maps'))

# Расставляем кнопки в 3 ряда по 2 штуки
keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6)

# Что бот сделает, когда ему напишут /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я твой первый бот. Выбери кнопку (сайт откроется прямо здесь!):", reply_markup=keyboard)

# Включаем бота. Он будет постоянно "слушать" Telegram
print("Бот начал работу! Чтобы остановить, нажми Ctrl+C в этом окне.")

bot.infinity_polling()
