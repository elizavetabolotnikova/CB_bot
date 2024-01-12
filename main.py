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
    if category == 'База данных':
        keys2 = {
            "МФО", "КПК", "СКЛК", "Ломбард", "СРО","Назад"
        }
        keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
        buttons = [types.KeyboardButton(text=key) for key in keys2]
        keyboard.add(*buttons)

        bot.send_message(message.chat.id, "Выберете категорию:", reply_markup=keyboard)
    elif category == 'Информация':
        bot.reply_to(message, "Основная информация о наших услугах и условиях предоставления микрозаймов.")
    elif category == 'FAQ':
        keys2 = {
            "МФО", "КПК", "СКЛК", "Ломбард", "СРО","Назад"
        }
        keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
        buttons = [types.KeyboardButton(text=key) for key in keys2]
        keyboard.add(*buttons)

        bot.send_message(message.chat.id, "Выберете категорию:", reply_markup=keyboard)
    elif category == 'Контакты':
        bot.reply_to(message, "Наши контактные данные: телефон - 123-456, email - example@example.com")
    else:
        bot.reply_to(message, "Извините, бот не может обработать этот запрос")

    @bot.message_handler(func=lambda message: message.text in keys2)
    def handle_subcategory(message: telebot.types.Message):
        subcategory = message.text
        if subcategory == 'МФО':
            bot.reply_to(message, "МФО - микрофинансовая организация")
        elif subcategory == 'КПК':
            bot.reply_to(message, "КПК - финансовая потребительская кооперация")
        elif subcategory == 'СКЛК':
            bot.reply_to(message, "СКЛК - специализированная потребительская кооперативная касса")
        elif subcategory == 'Ломбард':
            bot.reply_to(message, "Ломбард - учреждение, осуществляющее кредитование под залог движимого имущества")
        elif subcategory == 'СРО':
            bot.reply_to(message, "СРО - саморегулируемая организация")
        elif subcategory == 'Назад':
            keys = {
                'Информация',
                'База данных',
                'FAQ',
                'Контакты'
            }
            keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
            buttons = [types.KeyboardButton(text=key) for key in keys]
            keyboard.add(*buttons)

            bot.send_message(message.chat.id, "Выберете категорию:", reply_markup=keyboard)
        else:
            bot.reply_to(message, "Извините, бот не может обработать этот запрос")




bot.polling()
