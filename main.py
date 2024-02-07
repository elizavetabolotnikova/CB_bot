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
keys2 = {
            "МФО", "КПК", "СКЛК", "Ломбард", "СРО","Назад"
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
    simple_categories = {
        'Информация': "Основная информация о наших услугах и условиях предоставления микрозаймов.",
        'Контакты': "Наши контактные данные: телефон - 123-456, email - example@example.com"
    }
    keys2 = {
        "МФО", "КПК", "СКЛК", "Ломбард", "СРО","Назад"
    }
    default_message = "Извините, бот не может обработать этот запрос"
    if category == 'База данных':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
        buttons = [types.KeyboardButton(text=key) for key in keys2]
        keyboard.add(*buttons)

        bot.send_message(message.chat.id, "Выберете категорию:", reply_markup=keyboard)
    elif category == 'FAQ':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
        buttons = [types.KeyboardButton(text=key) for key in keys2]
        keyboard.add(*buttons)

        bot.send_message(message.chat.id, "Выберете категорию:", reply_markup=keyboard)
    else:
        bot.reply_to(message, simple_categories.get(category, default_message))

    @bot.message_handler(func=lambda message: message.text in keys2)
    def handle_subcategory(message: telebot.types.Message):
        subcategory = message.text
        keys = {
            'Информация',
            'База данных',
            'FAQ',
            'Контакты'
        }
        messages = {
            'МФО': "МФО - микрофинансовая организация",
            'КПК': "КПК - финансовая потребительская кооперация",
            'СКЛК': "СКЛК - специализированная потребительская кооперативная касса",
            'Ломбард': "Ломбард - учреждение, осуществляющее кредитование под залог движимого имущества",
            'СРО': "СРО - саморегулируемая организация"
        }
        default_message = "Извините, бот не может обработать этот запрос"
        if subcategory == 'Назад':
            keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
            buttons = [types.KeyboardButton(text=key) for key in keys]
            keyboard.add(*buttons)

            bot.send_message(message.chat.id, "Выберете категорию:", reply_markup=keyboard)
        else:
            bot.reply_to(message, messages.get(subcategory, default_message))




bot.polling()
