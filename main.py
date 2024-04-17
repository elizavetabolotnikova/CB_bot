import telebot
from telebot import types

TOKEN = "6987493385:AAFb4pcu4-PBtuYHyECEN22k_1qWQcMW6Gs"
keys = {
    'Информация',
    'Сбережения',
    'Заем',
    'Проверка надежности организации',
    'Проверка своей кредитной истории',
    'FAQ',
    'Контакты'
}
keys2 = {
    "МФК", "КПК", "СКПК", "Назад"
}
yes_no={"Да","Нет"}
yes_no2={"Да, хочу","Нет, не хочу"}
oline_ofline={'Хочу онлайн','Хочу офлайн'}
options = {"ИНН", "ОГРН", "Название", "Назад", "Меню"}
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = '''Я чат-бот, который поможет Вам узнать актуальную информацию о микрофинансовых организациях. Здесь Вы сможете найти ответы на все вопросы об условиях займов и сбережений, процентных ставках, сроках и прочих услугах. Начнём?'''
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

    if category == 'Сбережения':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
        buttons = [types.KeyboardButton(text=key) for key in yes_no]
        keyboard.add(*buttons)

        bot.send_message(message.chat.id, "Принято ли решение о типе организации:", reply_markup=keyboard)

        @bot.message_handler(func=lambda message: message.text in yes_no)
        def handle_subcategory(message: telebot.types.Message):
            subcategory = message.text
            if subcategory == 'Да':
                keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                buttons = [types.KeyboardButton(text=key) for key in keys2]
                keyboard.add(*buttons)
                bot.send_message(message.chat.id, "Выберете категорию:", reply_markup=keyboard)
            if subcategory == 'Нет':
                keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                buttons = [types.KeyboardButton(text=key) for key in yes_no2]
                keyboard.add(*buttons)
                bot.send_message(message.chat.id, "Хотите узнать больше про все типы организаций?", reply_markup=keyboard)

                @bot.message_handler(func=lambda message: message.text in yes_no2)
                def handle_subcategory(message: telebot.types.Message):
                    subcategory = message.text
                    if subcategory == 'Да, хочу':
                        options2 = {"Информация о МФО", "Информация о КПК", "Информация о СКПК",
                                    "Информация о Ломбардах",
                                    "Информация о СРО", "Назад", "Меню"}
                        keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                        buttons = [types.KeyboardButton(text=key) for key in options2]
                        keyboard.add(*buttons)
                        bot.send_message(message.chat.id, "Выберете категорию:", reply_markup=keyboard)
                    if subcategory == 'Нет, не хочу':
                        keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                        buttons = [types.KeyboardButton(text=key) for key in oline_ofline]
                        keyboard.add(*buttons)
                        bot.send_message(message.chat.id, "Хотите онлайн?",
                                        reply_markup=keyboard)

                        @bot.message_handler(func=lambda message: message.text in oline_ofline)
                        def handle_subcategory(message: telebot.types.Message):
                            subcategory = message.text
                            if subcategory == 'Хочу онлайн':
                                often = {'Редо','Часто'}
                                keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                                buttons = [types.KeyboardButton(text=key) for key in often]
                                keyboard.add(*buttons)
                                bot.send_message(message.chat.id, "Как часто Вы пользуетесь сбережениями?", reply_markup=keyboard)
                            if subcategory == 'Хочу офлайн':
                                response = {'Хорошо', 'Нет, спасибо'}
                                keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                                buttons = [types.KeyboardButton(text=key) for key in response]
                                keyboard.add(*buttons)
                                bot.send_message(message.chat.id, "Тогда рекомендуем Вам обратиться в МФО. Обратите внимание  минимальный размер инвестиций в МФК для граждан и индивидуальных предпринимателей — 1,5 млн рублей.",
                                                 reply_markup=keyboard)
        @bot.message_handler(func=lambda message: message.text in keys2)
        def handle_subcategory1(message: telebot.types.Message):
            subcategory = message.text

            options = {"ИНН", "ОГРН", "Название", "Назад", "Меню"}
            if subcategory == 'Назад':
                keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                buttons = [types.KeyboardButton(text=key) for key in keys]
                keyboard.add(*buttons)

                bot.send_message(message.chat.id, "Выберете категорию:", reply_markup=keyboard)
            elif subcategory in ["МФК", "КПК", "СКПК", "Ломбард"]:
                keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                buttons = [types.KeyboardButton(text=key) for key in options]
                keyboard.add(*buttons)

                bot.send_message(message.chat.id, "По какому признаку вы хотите выбрать организацию:", reply_markup=keyboard)

                @bot.message_handler(func=lambda message: message.text in options)
                def handle_subcategory2(message: telebot.types.Message):
                    subcategory = message.text
                    if subcategory == "ИНН":
                        bot.send_message(message.chat.id, "Введите ИНН:")
                    elif subcategory == "ОГРН":
                        bot.send_message(message.chat.id, "Введите ОГРН:")
                    elif subcategory == "Название":
                        bot.send_message(message.chat.id, "Введите Название:")
            else:
                bot.reply_to(message, messages.get(subcategory, "Извините, бот не может обработать этот запрос"))


    if category == 'FAQ':
        options2 = {"Информация о МФО", "Информация о КПК", "Информация о СКПК", "Информация о Ломбардах",
                    "Информация о СРО", "Назад", "Меню"}
        keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
        buttons = [types.KeyboardButton(text=key) for key in options2]
        keyboard.add(*buttons)

        bot.send_message(message.chat.id, "Выберете категорию:", reply_markup=keyboard)

        @bot.message_handler(func=lambda message: message.text in options2)
        def handle_subcategory4(message: telebot.types.Message):
            subcategory = message.text
            questions_mfo = {
                "Что такое МФО и как они работают?",
                "Как выбрать подходящую МФО?",
                "Какова процедура получения займа?",
                "Какая информация обязательна при заполнении заявки?",
                "Как долго занимает процесс рассмотрения заявки?",
                "Как осуществляется погашение займа?",
                "Что происходит, если я не могу погасить займ вовремя?", "Назад", "Меню"
            }
            questions_kpk = {"Что такое кредитный потребительский кооператив?",
                             "Как стать членом КПК?",
                             "Какие услуги предоставляют КПК?",
                             "Каковы преимущества членства в КПК по сравнению с обычным банком?",
                             "Что такое лояльность КПК?",
                             "Какие гарантии безопасности при хранении средств в КПК?",
                             "Как часто можно получать кредиты от КПК?",
                             "Как получить подробную информацию о КПК и их услугах?", "Назад"
                             }
            questions_sklk = {"Что такое сельскохозяйственный кредитный потребительский кооператив (СКПК)?",
                              "Каков процесс вступления в члены СКПК?",
                              "Какие виды финансовых услуг предоставляются СКПК своим членам?",
                              "В чем преимущества участия в СКПК по сравнению с другими финансовыми институтами?",
                              "Как кооператив поддерживает сельскохозяйственное развитие?",
                              "Каковы условия возврата кредитов в СКПК?",
                              "Как члены могут влиять на принятие решений в СКПК?", "Назад"
                              }
            questions_lombard = {"Что такое ломбард?",
                                 "Какие услуги предоставляет ломбард?",
                                 "Как получить заем от ломбарда?",
                                 "Каковы преимущества залогового кредитования?",
                                 "Какие сроки и процентные ставки у ломбарда?",
                                 "Что происходит, если я не могу погасить займ в ломбарде?",
                                 "Можно ли получить залоговый кредит, если предмет не принадлежит мне полностью?",
                                 "Как выбрать ломбард с хорошей репутацией?", "Назад"
                                 }
            questions_sro = {"Что такое СРО?",
                             "Для чего создаются СРО?",
                             "Кто может быть членом СРО?",
                             "Как стать членом СРО?",
                             "Какие преимущества членства в СРО?",
                             "Какова роль СРО в надзоре за своими членами?",
                             "Какие санкции могут быть наложены СРО на своих членов?",
                             "Как получить информацию о СРО и их деятельности?"
                             }
            if subcategory == "Информация о МФО":
                keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                buttons = [types.KeyboardButton(text=key) for key in questions_mfo]
                keyboard.add(*buttons)
                bot.send_message(message.chat.id, "Выберете вопрос:", reply_markup=keyboard)

                @bot.message_handler(func=lambda message: message.text in questions_mfo)
                def handle_subcategory(message: telebot.types.Message):
                    subcategory = message.text
                    messages = {
                        "Что такое МФО и как они работают?": "МФО (микрофинансовые организации) предоставляют короткосрочные займы физическим лицам и малому бизнесу. Они часто работают онлайн и упрощают процесс получения кредита, поскольку не требуют большого количества документов и предлагают быстрое одобрение заявки.",
                        "Как выбрать подходящую МФО?": "При выборе МФО важно учитывать такие факторы, как процентная ставка по кредиту, сроки погашения, условия для получения займа и надежность компании. Также полезно ознакомиться с отзывами других пользователей, чтобы получить представление о качестве обслуживания.",
                        "Какова процедура получения займа?": "Процедура получения займа в МФО обычно очень проста и удобна. Вы должны заполнить онлайн-заявку, указав необходимую сумму и срок кредита, а также предоставить несколько документов (обычно паспорт и ИНН). Затем заявка рассматривается, и если она одобрена, деньги переводятся на ваш счет.",
                        "Какая информация обязательна при заполнении заявки?": "Обычно при заполнении заявки в МФО требуется указать личную информацию, такую как ФИО, дата рождения, адрес проживания, контактные данные. Некоторые МФО могут также запросить информацию о доходах, семейном положении и т.д.",
                        "Как долго занимает процесс рассмотрения заявки?": "Время рассмотрения заявки в МФО может варьироваться, обычно это занимает от нескольких минут до нескольких часов. Некоторые компании могут предлагать быстрое одобрение за несколько минут, но это зависит от политики каждой конкретной МФО. В любом случае, МФО обычно стараются обеспечить быструю обработку заявок и перевод денег.",
                        "Как осуществляется погашение займа?": "Погашение займа в МФО обычно осуществляется путем перевода суммы платежа на счет МФО в указанный срок. Сумма платежа включает сумму основного долга и проценты, которые были оговорены в договоре. В некоторых случаях можно выбрать способ погашения займа, оплатив с помощью банковской карты или электронного кошелька.",
                        "Что происходит, если я не могу погасить займ вовремя?": "В случае, если вы не можете погасить займ вовремя, вам следует связаться с МФО и подробно объяснить свою ситуацию. МФО могут предложить вам определенные варианты, такие как продление срока кредита или установка рассрочки. Важно не игнорировать проблему и своевременно обратиться за помощью."}
                    default_message = "Извините, бот не может обработать этот запрос"
                    if subcategory == 'Назад':
                        keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                        buttons = [types.KeyboardButton(text=key) for key in options2]
                        keyboard.add(*buttons)

                        bot.send_message(message.chat.id, "Выберете категорию:", reply_markup=keyboard)
                    else:
                        bot.reply_to(message, messages.get(subcategory, default_message))
            elif subcategory == "Информация о КПК":
                keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                buttons = [types.KeyboardButton(text=key) for key in questions_kpk]
                keyboard.add(*buttons)
                bot.send_message(message.chat.id, "Выберете вопрос:", reply_markup=keyboard)

                @bot.message_handler(func=lambda message: message.text in questions_kpk)
                def handle_subcategory(message: telebot.types.Message):
                    subcategory = message.text
                    messages = {
                        "Что такое кредитный потребительский кооператив?": "КПК – это финансовая организация, основанная на членстве, которая предоставляет кредиты, сбережения и другие финансовые услуги своим членам.",
                        "Как стать членом КПК?": "Обычно для становления членом КПК необходимо заполнить анкету, внести определенную сумму доли и уплатить членский взнос. Точная процедура может отличаться от КПК к КПК.",
                        "Какие услуги предоставляют КПК?": "КПК обычно предлагают кредиты под различные потребности (автокредиты, ипотека и т.д.), вклады, сберегательные счета, услуги по денежному переводу и прочие банковские услуги.",
                        "Каковы преимущества членства в КПК по сравнению с обычным банком?": "Членами КПК являются его владельцы, поэтому они могут получать более высокую доходность на свои вклады, более низкие процентные ставки на кредиты и могут принимать участие в управлении кооперативом.",
                        "Что такое лояльность КПК?": "Лояльность КПК – это способ оценки преданности и доверия членов кооператива. Члены, которые используют и рекомендуют услуги КПК, могут получать дополнительные преимущества и вознаграждения.",
                        "Какие гарантии безопасности при хранении средств в КПК?": "КПК обычно защищены гарантией страхования депозитов, которая покрывает потерю средств в случае банкротства КПК.",
                        "Как часто можно получать кредиты от КПК?": "Частота предоставления кредитов зависит от политики каждого КПК, но обычно члены могут получать кредиты по мере необходимости, соблюдая установленные правила и условия.",
                        "Как получить подробную информацию о КПК и их услугах?": "Лучший способ получить информацию о конкретном КПК – это посетить их веб-сайт, побеседовать с сотрудниками и прочитать отзывы или рекомендации других членов."}
                    default_message = "Извините, бот не может обработать этот запрос"
                    if subcategory == 'Назад':
                        keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                        buttons = [types.KeyboardButton(text=key) for key in options2]
                        keyboard.add(*buttons)

                        bot.send_message(message.chat.id, "Выберете категорию:", reply_markup=keyboard)
                    else:
                        bot.reply_to(message, messages.get(subcategory, default_message))
            elif subcategory == "Информация о СКЛК":
                keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                buttons = [types.KeyboardButton(text=key) for key in questions_sklk]
                keyboard.add(*buttons)
                bot.send_message(message.chat.id, "Выберете вопрос:", reply_markup=keyboard)

                @bot.message_handler(func=lambda message: message.text in questions_sklk)
                def handle_subcategory(message: telebot.types.Message):
                    subcategory = message.text
                    messages = {
                        "Что такое сельскохозяйственный кредитный потребительский кооператив (СКПК)?": "СКПК – это кооперативная организация, созданная на основе членства фермеров и других участников сельского хозяйства, предоставляющая финансовую поддержку, кредиты и другие услуги для развития сельского общества.",
                        "Каков процесс вступления в члены СКПК?": "Обычно, для вступления в члены СКПК требуется подача заявления, оплата членского взноса и соблюдение установленных критериев членства, которые могут включать статус фермера или предпринимателя в сельском хозяйстве.",
                        "Какие виды финансовых услуг предоставляются СКПК своим членам?": "СКПК предоставляют кредиты для сельскохозяйственных нужд, сберегательные счета, страхование, финансовые консультации и другие услуги, направленные на поддержку устойчивости и развития сельского хозяйства.",
                        "В чем преимущества участия в СКПК по сравнению с другими финансовыми институтами?": "Члены СКПК могут получать более доступные кредиты, специализированные услуги для сельского хозяйства, участвовать в принятии решений по управлению кооперативом и обладать определенными финансовыми привилегиями.",
                        "Как кооператив поддерживает сельскохозяйственное развитие?": "СКПК предоставляют финансовую поддержку для закупки сельскохозяйственного оборудования, улучшения инфраструктуры, обучения фермеров, а также содействуют реализации инновационных проектов в сельском хозяйстве.",
                        "Каковы условия возврата кредитов в СКПК?": "Условия возврата кредитов зависят от политики каждого СКПК, но обычно включают гибкий график платежей, учитывающий сезонные особенности сельского хозяйства, и различные программы поддержки в случае временных трудностей.",
                        "Как члены могут влиять на принятие решений в СКПК?": "Члены СКПК обычно имеют право голоса на собраниях и выборах, где принимаются ключевые решения. Участие членов в управлении кооперативом обеспечивает демократичность и прозрачность в принятии важных решений."}
                    default_message = "Извините, бот не может обработать этот запрос"
                    if subcategory == 'Назад':
                        keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                        buttons = [types.KeyboardButton(text=key) for key in options2]
                        keyboard.add(*buttons)

                        bot.send_message(message.chat.id, "Выберете категорию:", reply_markup=keyboard)
                    else:
                        bot.reply_to(message, messages.get(subcategory, default_message))
            elif subcategory == "Информация о Ломбардах":
                keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                buttons = [types.KeyboardButton(text=key) for key in questions_lombard]
                keyboard.add(*buttons)
                bot.send_message(message.chat.id, "Выберете вопрос:", reply_markup=keyboard)

                @bot.message_handler(func=lambda message: message.text in questions_lombard)
                def handle_subcategory(message: telebot.types.Message):
                    subcategory = message.text
                    messages = {
                        "Что такое ломбард?": "Ломбард - это финансовая организация, где вы можете получить заем, предоставив в залог ценные вещи, такие как ювелирные изделия, электроника, автомобиль и т.д.",
                        "Какие услуги предоставляет ломбард?": "Ломбард предоставляет услуги залогового кредитования, где вы можете получить деньги в обмен на залог предметов. Они также могут предлагать услуги по выкупу заложенных предметов или продаже залогового имущества.",
                        "Как получить заем от ломбарда?": "Для получения займа от ломбарда, вам необходимо предоставить ценную вещь в залог. Ломбард произведет оценку предмета и предложит вам сумму займа в зависимости от его стоимости и оценки.",
                        "Каковы преимущества залогового кредитования?": "Залоговое кредитование может быть преимущественным способом получения займа, особенно если у вас есть нестабильный кредитный рейтинг или отсутствует другая возможность получить кредит. Кроме того, процесс получения займа относительно прост и быстр.",
                        "Какие сроки и процентные ставки у ломбарда?": "Сроки и процентные ставки в ломбардах могут различаться. Обычно займы предоставляются на короткий срок от нескольких недель до нескольких месяцев, и ставки могут быть разными в зависимости от правил и политики конкретного ломбарда.",
                        "Что происходит, если я не могу погасить займ в ломбарде?": "Если вы не можете погасить займ в ломбарде вовремя, они могут отобрать предмет, который был заложен в качестве залога, и продать его, чтобы покрыть задолженность по займу. Остаток суммы после продажи предмета возвращается вам.",
                        "Можно ли получить залоговый кредит, если предмет не принадлежит мне полностью?": "Обычно ломбарды требуют, чтобы предмет, выступающий в качестве залога, был полностью в вашей собственности без других обременений или прав третьих лиц.",
                        "Как выбрать ломбард с хорошей репутацией?": "При выборе ломбарда, рекомендуется обратить внимание на репутацию, отзывы и условия, предлагаемые различными ломбардами. Также полезно обратиться за советом к знакомым или рекомендациям, чтобы выбрать надежный и ответственный ломбард."
                    }
                    default_message = "Извините, бот не может обработать этот запрос"
                    if subcategory == 'Назад':
                        keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                        buttons = [types.KeyboardButton(text=key) for key in options2]
                        keyboard.add(*buttons)

                        bot.send_message(message.chat.id, "Выберете категорию:", reply_markup=keyboard)
                    else:
                        bot.reply_to(message, messages.get(subcategory, default_message))
            elif subcategory == "Информация о СРО":
                keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                buttons = [types.KeyboardButton(text=key) for key in questions_sro]
                keyboard.add(*buttons)
                bot.send_message(message.chat.id, "Выберете вопрос:", reply_markup=keyboard)

                @bot.message_handler(func=lambda message: message.text in questions_sro)
                def handle_subcategory(message: telebot.types.Message):
                    subcategory = message.text
                    messages = {
                        "Что такое СРО?": "СРО (саморегулируемая организация) – это организация, созданная в рамках определенной отрасли для саморегулирования и надзора за деятельностью своих членов. СРО устанавливают правила и стандарты, которым должны следовать ее члены.",
                        "Для чего создаются СРО?": "СРО создаются для обеспечения надлежащего качества и безопасности услуг или работ в определенной отрасли. Они контролируют деятельность своих членов, разрабатывают общепринятые стандарты и регулируют сферу деятельности.",
                        "Кто может быть членом СРО?": "Членами СРО могут быть юридические и физические лица, включая компании и специалистов, работающих в соответствующей отрасли. Членство в СРО обычно является добровольным, однако в некоторых случаях оно может быть обязательным.",
                        "Как стать членом СРО?": "Процесс вступления в СРО может различаться в зависимости от конкретной организации и ее правил. Обычно требуется подать заявку, предоставить необходимые документы, выполнить определенные условия, такие как обучение или стажировка, и уплатить членские взносы.",
                        "Какие преимущества членства в СРО?": "Членство в СРО может предоставлять ряд преимуществ. Это может включать доступ к информации и ресурсам, повышение доверия и репутации в отрасли, защиту прав и интересов членов, а также возможность повышения профессионального уровня.",
                        "Какова роль СРО в надзоре за своими членами?": "СРО осуществляет надзор и контроль за деятельностью своих членов. Они могут проводить проверки, аудиты, разрабатывать правила и нормативы, а также рассматривать жалобы и принимать меры в отношении нарушителей.",
                        "Какие санкции могут быть наложены СРО на своих членов?": "СРО могут применять различные санкции к своим членам в случае нарушения правил и стандартов. Это может включать штрафы, ограничения в деятельности, аннулирование членства или другие меры в соответствии с уставом организации.",
                        "Как получить информацию о СРО и их деятельности?": "Для получения подробной информации о конкретном СРО можно обратиться на их официальные веб-сайты, изучить их устав и правила, а также проконсультироваться у представителей организации или других профессионалов в отрасли."
                    }
                    default_message = "Извините, бот не может обработать этот запрос"
                    if subcategory == 'Назад':
                        keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                        buttons = [types.KeyboardButton(text=key) for key in options2]
                        keyboard.add(*buttons)

                        bot.send_message(message.chat.id, "Выберете категорию:", reply_markup=keyboard)
                    else:
                        bot.reply_to(message, messages.get(subcategory, default_message))
            elif subcategory == "Меню":
                keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                buttons = [types.KeyboardButton(text=key) for key in keys]
                keyboard.add(*buttons)

                bot.send_message(message.chat.id, "Выберете категорию:", reply_markup=keyboard)
    if category == 'Проверка своей кредитной истории':
        text='Вы можете воспользоваться услугами БКИ(ссылка)'
        bot.reply_to(message, text)
        text2='Также на сайте (ссылка) вы можете посмотреть подробную пошаговую инструкцию по проверке своей кредитной истории'
        bot.reply_to(message, text2)
    if category == 'Проверка надежности организации':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
        buttons = [types.KeyboardButton(text=key) for key in options]
        keyboard.add(*buttons)
        bot.send_message(message.chat.id, "Выберете категорию:", reply_markup=keyboard)


bot.polling()
