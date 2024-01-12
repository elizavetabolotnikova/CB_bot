import telebot
import requests
import json
from telebot import types

TOKEN = "6987493385:AAFb4pcu4-PBtuYHyECEN22k_1qWQcMW6Gs"
keys = {
    'Информация',
    'База данных',
    'FAQ',
    'Контакты'
}

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = '''Привет и добро пожаловать в нашего Telegram-бота по микрозаймам! 

Я готов помочь тебе получить информацию, ознакомиться с нашей базой данных, ответить на часто задаваемые вопросы и предоставить контактные данные для связи с нами. 

Выбери одну из четырех кнопок ниже, чтобы начать: 

- "Информация" - узнай больше о наших услугах и условиях предоставления микрозаймов. 
- "База данных" - получи доступ к нашей базе данных с информацией о наших клиентах и текущих займах. 
- "FAQ" - получи ответы на часто задаваемые вопросы о микрозаймах и нашем боте. 
- "Контакты" - свяжись с нами для получения дополнительной помощи и консультаций. 

Если у тебя возникнут вопросы или тебе потребуется специальная помощь, не стесняйся обратиться к нам! Мы готовы помочь тебе получить нужный микрозайм и решить твои финансовые вопросы. 

Удачи и надеюсь, что наш Telegram-бот будет полезным для тебя!'''
    bot.reply_to(message, text)

    keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
    buttons = [types.KeyboardButton(text=key) for key in keys]
    keyboard.add(*buttons)

    bot.send_message(message.chat.id, "Выберете категорию:", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text in keys)
def handle_category(message: telebot.types.Message):
    category = message.text
    if category == 'База данных':
        bot.reply_to(message, "Вы выбрали: Вопросы по документам. Задайте свой вопрос")
    elif category == 'Информация':
        bot.reply_to(message, "Вы выбрали: Вопросы по навигации. Задайте свой вопрос")
    elif category == 'FAQ':
        bot.reply_to(message, "Вы выбрали: Вопросы по личной эффективности. Задайте свой вопрос")
    elif category == 'FAQ':
        bot.reply_to(message, "Вы выбрали: Вопросы по личной эффективности. Задайте свой вопрос")
    else:
        bot.reply_to(message, "Извините, я не могу ответить на этот вопрос.")


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    user_text = message.text
    if user_text == 'Где оформить заявление на отпуск?':
        bot.reply_to(message, "Перейдите в раздел")
    # Отправляем запрос к OpenAI API, используя ваш API ключ


bot.polling()
