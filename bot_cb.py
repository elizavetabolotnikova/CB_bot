import requests
import telebot
from telebot import types

res1 = requests.get('http://localhost:3000/organization')
res2 = requests.get('http://localhost:3000/products')
products = res2.json()
organizations = res1.json()
TOKEN = '6987493385:AAFb4pcu4-PBtuYHyECEN22k_1qWQcMW6Gs'
keys = {
    'Сбережения',
    'Заем',
    'Проверка надежности организации',
    'Проверка своей кредитной истории',
    'FAQ',
    'Контакты'
}
keys2 = {
    'МФК', 'КПК', 'СКПК', 'Меню'
}
keys3 = {'Хочу взять заем в МФК', 'Хочу взять заем в МКК', 'Хочу взять заем в КПК', 'Хочу взять заем в СКПК',
         'Хочу взять заем в Ломбарде', 'Меню'}

yes_no = {'Да', 'Нет', 'Меню'}
yes_no2 = {'Да, хочу', 'Нет, не хочу', 'Меню'}
yes_no3 = {'Да, принято', 'Нет, не принято', 'Меню'}
yes_no4 = {'Хочу', 'Не хочу', 'Меню'}
online_ofline = {'Онлайн', 'Офлайн', 'Меню'}
online_ofline2 = {'Хочу онлайн', 'Хочу офлайн', 'Меню'}
often = {'Редко', 'Регулярно', 'Меню'}
often2 = {'Часто', 'Иногда', 'Меню'}
options = {'ИНН', 'ОГРН', 'Название', 'Меню'}
options2 = {'Информация о МФО', 'Информация о КПК', 'Информация о СКПК', 'Информация о Ломбардах',
            'Информация о СРО', 'Меню'}
bot = telebot.TeleBot(TOKEN)
type_org = []
online_bool = False


def faq():
    @bot.message_handler(func=lambda message: message.text in options2)
    def handle_subcategory4(message: telebot.types.Message):
        subcategory = message.text
        questions_mfo = {
            'Что такое МФО и как они работают?',
            'Как выбрать подходящую МФО?',
            'Какова процедура получения займа?',
            'Какая информация обязательна при заполнении заявки?',
            'Как долго занимает процесс рассмотрения заявки?',
            'Как осуществляется погашение займа?',
            'Что происходит, если я не могу погасить займ вовремя?', 'Меню', 'Назад'
        }
        questions_kpk = {'Что такое кредитный потребительский кооператив?',
                         'Как стать членом КПК?',
                         'Какие услуги предоставляют КПК?',
                         'Каковы преимущества членства в КПК по сравнению с обычным банком?',
                         'Что такое лояльность КПК?',
                         'Какие гарантии безопасности при хранении средств в КПК?',
                         'Как часто можно получать кредиты от КПК?',
                         'Как получить подробную информацию о КПК и их услугах?', 'Меню', 'Назад'
                         }
        questions_sklk = {'Что такое сельскохозяйственный кредитный потребительский кооператив (СКПК)?',
                          'Каков процесс вступления в члены СКПК?',
                          'Какие виды финансовых услуг предоставляются СКПК своим членам?',
                          'В чем преимущества участия в СКПК по сравнению с другими финансовыми институтами?',
                          'Как кооператив поддерживает сельскохозяйственное развитие?',
                          'Каковы условия возврата кредитов в СКПК?',
                          'Как члены могут влиять на принятие решений в СКПК?', 'Меню', 'Назад'
                          }
        questions_lombard = {'Что такое ломбард?',
                             'Какие услуги предоставляет ломбард?',
                             'Как получить заем от ломбарда?',
                             'Каковы преимущества залогового кредитования?',
                             'Какие сроки и процентные ставки у ломбарда?',
                             'Что происходит, если я не могу погасить займ в ломбарде?',
                             'Можно ли получить залоговый кредит, если предмет не принадлежит мне полностью?',
                             'Как выбрать ломбард с хорошей репутацией?', 'Меню', 'Назад'
                             }
        questions_sro = {'Что такое СРО?',
                         'Для чего создаются СРО?',
                         'Кто может быть членом СРО?',
                         'Как стать членом СРО?',
                         'Какие преимущества членства в СРО?',
                         'Какова роль СРО в надзоре за своими членами?',
                         'Какие санкции могут быть наложены СРО на своих членов?',
                         'Как получить информацию о СРО и их деятельности?', 'Меню', 'Назад'
                         }
        if subcategory == 'Информация о МФО':
            keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
            buttons = [types.KeyboardButton(text=key) for key in questions_mfo]
            keyboard.add(*buttons)
            bot.send_message(message.chat.id, 'Выберете вопрос:', reply_markup=keyboard)

            @bot.message_handler(func=lambda message: message.text in questions_mfo)
            def handle_subcategory(message: telebot.types.Message):
                subcategory = message.text
                messages = {
                    'Что такое МФО и как они работают?': 'МФО (микрофинансовые организации) предоставляют короткосрочные займы физическим лицам и малому бизнесу. Они часто работают онлайн и упрощают процесс получения кредита, поскольку не требуют большого количества документов и предлагают быстрое одобрение заявки.',
                    'Как выбрать подходящую МФО?': 'При выборе МФО важно учитывать такие факторы, как процентная ставка по кредиту, сроки погашения, условия для получения займа и надежность компании. Также полезно ознакомиться с отзывами других пользователей, чтобы получить представление о качестве обслуживания.',
                    'Какова процедура получения займа?': 'Процедура получения займа в МФО обычно очень проста и удобна. Вы должны заполнить онлайн-заявку, указав необходимую сумму и срок кредита, а также предоставить несколько документов (обычно паспорт и ИНН). Затем заявка рассматривается, и если она одобрена, деньги переводятся на ваш счет.',
                    'Какая информация обязательна при заполнении заявки?': 'Обычно при заполнении заявки в МФО требуется указать личную информацию, такую как ФИО, дата рождения, адрес проживания, контактные данные. Некоторые МФО могут также запросить информацию о доходах, семейном положении и т.д.',
                    'Как долго занимает процесс рассмотрения заявки?': 'Время рассмотрения заявки в МФО может варьироваться, обычно это занимает от нескольких минут до нескольких часов. Некоторые компании могут предлагать быстрое одобрение за несколько минут, но это зависит от политики каждой конкретной МФО. В любом случае, МФО обычно стараются обеспечить быструю обработку заявок и перевод денег.',
                    'Как осуществляется погашение займа?': 'Погашение займа в МФО обычно осуществляется путем перевода суммы платежа на счет МФО в указанный срок. Сумма платежа включает сумму основного долга и проценты, которые были оговорены в договоре. В некоторых случаях можно выбрать способ погашения займа, оплатив с помощью банковской карты или электронного кошелька.',
                    'Что происходит, если я не могу погасить займ вовремя?': 'В случае, если вы не можете погасить займ вовремя, вам следует связаться с МФО и подробно объяснить свою ситуацию. МФО могут предложить вам определенные варианты, такие как продление срока кредита или установка рассрочки. Важно не игнорировать проблему и своевременно обратиться за помощью.'}
                default_message = 'Извините, бот не может обработать этот запрос'
                if subcategory == 'Назад':
                    keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                    buttons = [types.KeyboardButton(text=key) for key in options2]
                    keyboard.add(*buttons)

                    bot.send_message(message.chat.id, 'Выберете категорию:', reply_markup=keyboard)
                else:
                    bot.reply_to(message, messages.get(subcategory, default_message))
        elif subcategory == 'Информация о КПК':
            keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
            buttons = [types.KeyboardButton(text=key) for key in questions_kpk]
            keyboard.add(*buttons)
            bot.send_message(message.chat.id, 'Выберете вопрос:', reply_markup=keyboard)

            @bot.message_handler(func=lambda message: message.text in questions_kpk)
            def handle_subcategory(message: telebot.types.Message):
                subcategory = message.text
                messages = {
                    'Что такое кредитный потребительский кооператив?': 'КПК – это финансовая организация, основанная на членстве, которая предоставляет кредиты, сбережения и другие финансовые услуги своим членам.',
                    'Как стать членом КПК?': 'Обычно для становления членом КПК необходимо заполнить анкету, внести определенную сумму доли и уплатить членский взнос. Точная процедура может отличаться от КПК к КПК.',
                    'Какие услуги предоставляют КПК?': 'КПК обычно предлагают кредиты под различные потребности (автокредиты, ипотека и т.д.), вклады, сберегательные счета, услуги по денежному переводу и прочие банковские услуги.',
                    'Каковы преимущества членства в КПК по сравнению с обычным банком?': 'Членами КПК являются его владельцы, поэтому они могут получать более высокую доходность на свои вклады, более низкие процентные ставки на кредиты и могут принимать участие в управлении кооперативом.',
                    'Что такое лояльность КПК?': 'Лояльность КПК – это способ оценки преданности и доверия членов кооператива. Члены, которые используют и рекомендуют услуги КПК, могут получать дополнительные преимущества и вознаграждения.',
                    'Какие гарантии безопасности при хранении средств в КПК?': 'КПК обычно защищены гарантией страхования депозитов, которая покрывает потерю средств в случае банкротства КПК.',
                    'Как часто можно получать кредиты от КПК?': 'Частота предоставления кредитов зависит от политики каждого КПК, но обычно члены могут получать кредиты по мере необходимости, соблюдая установленные правила и условия.',
                    'Как получить подробную информацию о КПК и их услугах?': 'Лучший способ получить информацию о конкретном КПК – это посетить их веб-сайт, побеседовать с сотрудниками и прочитать отзывы или рекомендации других членов.'}
                default_message = 'Извините, бот не может обработать этот запрос'
                if subcategory == 'Назад':
                    keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                    buttons = [types.KeyboardButton(text=key) for key in options2]
                    keyboard.add(*buttons)

                    bot.send_message(message.chat.id, 'Выберете категорию:', reply_markup=keyboard)
                else:
                    bot.reply_to(message, messages.get(subcategory, default_message))
        elif subcategory == 'Информация о СКПК':
            keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
            buttons = [types.KeyboardButton(text=key) for key in questions_sklk]
            keyboard.add(*buttons)
            bot.send_message(message.chat.id, 'Выберете вопрос:', reply_markup=keyboard)

            @bot.message_handler(func=lambda message: message.text in questions_sklk)
            def handle_subcategory(message: telebot.types.Message):
                subcategory = message.text
                messages = {
                    'Что такое сельскохозяйственный кредитный потребительский кооператив (СКПК)?': 'СКПК – это кооперативная организация, созданная на основе членства фермеров и других участников сельского хозяйства, предоставляющая финансовую поддержку, кредиты и другие услуги для развития сельского общества.',
                    'Каков процесс вступления в члены СКПК?': 'Обычно, для вступления в члены СКПК требуется подача заявления, оплата членского взноса и соблюдение установленных критериев членства, которые могут включать статус фермера или предпринимателя в сельском хозяйстве.',
                    'Какие виды финансовых услуг предоставляются СКПК своим членам?': 'СКПК предоставляют кредиты для сельскохозяйственных нужд, сберегательные счета, страхование, финансовые консультации и другие услуги, направленные на поддержку устойчивости и развития сельского хозяйства.',
                    'В чем преимущества участия в СКПК по сравнению с другими финансовыми институтами?': 'Члены СКПК могут получать более доступные кредиты, специализированные услуги для сельского хозяйства, участвовать в принятии решений по управлению кооперативом и обладать определенными финансовыми привилегиями.',
                    'Как кооператив поддерживает сельскохозяйственное развитие?': 'СКПК предоставляют финансовую поддержку для закупки сельскохозяйственного оборудования, улучшения инфраструктуры, обучения фермеров, а также содействуют реализации инновационных проектов в сельском хозяйстве.',
                    'Каковы условия возврата кредитов в СКПК?': 'Условия возврата кредитов зависят от политики каждого СКПК, но обычно включают гибкий график платежей, учитывающий сезонные особенности сельского хозяйства, и различные программы поддержки в случае временных трудностей.',
                    'Как члены могут влиять на принятие решений в СКПК?': 'Члены СКПК обычно имеют право голоса на собраниях и выборах, где принимаются ключевые решения. Участие членов в управлении кооперативом обеспечивает демократичность и прозрачность в принятии важных решений.'}
                default_message = 'Извините, бот не может обработать этот запрос'
                if subcategory == 'Назад':
                    keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                    buttons = [types.KeyboardButton(text=key) for key in options2]
                    keyboard.add(*buttons)

                    bot.send_message(message.chat.id, 'Выберете категорию:', reply_markup=keyboard)
                else:
                    bot.reply_to(message, messages.get(subcategory, default_message))
        elif subcategory == 'Информация о Ломбардах':
            keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
            buttons = [types.KeyboardButton(text=key) for key in questions_lombard]
            keyboard.add(*buttons)
            bot.send_message(message.chat.id, 'Выберете вопрос:', reply_markup=keyboard)

            @bot.message_handler(func=lambda message: message.text in questions_lombard)
            def handle_subcategory(message: telebot.types.Message):
                subcategory = message.text
                messages = {
                    'Что такое ломбард?': 'Ломбард - это финансовая организация, где вы можете получить заем, предоставив в залог ценные вещи, такие как ювелирные изделия, электроника, автомобиль и т.д.',
                    'Какие услуги предоставляет ломбард?': 'Ломбард предоставляет услуги залогового кредитования, где вы можете получить деньги в обмен на залог предметов. Они также могут предлагать услуги по выкупу заложенных предметов или продаже залогового имущества.',
                    'Как получить заем от ломбарда?': 'Для получения займа от ломбарда, вам необходимо предоставить ценную вещь в залог. Ломбард произведет оценку предмета и предложит вам сумму займа в зависимости от его стоимости и оценки.',
                    'Каковы преимущества залогового кредитования?': 'Залоговое кредитование может быть преимущественным способом получения займа, особенно если у вас есть нестабильный кредитный рейтинг или отсутствует другая возможность получить кредит. Кроме того, процесс получения займа относительно прост и быстр.',
                    'Какие сроки и процентные ставки у ломбарда?': 'Сроки и процентные ставки в ломбардах могут различаться. Обычно займы предоставляются на короткий срок от нескольких недель до нескольких месяцев, и ставки могут быть разными в зависимости от правил и политики конкретного ломбарда.',
                    'Что происходит, если я не могу погасить займ в ломбарде?': 'Если вы не можете погасить займ в ломбарде вовремя, они могут отобрать предмет, который был заложен в качестве залога, и продать его, чтобы покрыть задолженность по займу. Остаток суммы после продажи предмета возвращается вам.',
                    'Можно ли получить залоговый кредит, если предмет не принадлежит мне полностью?': 'Обычно ломбарды требуют, чтобы предмет, выступающий в качестве залога, был полностью в вашей собственности без других обременений или прав третьих лиц.',
                    'Как выбрать ломбард с хорошей репутацией?': 'При выборе ломбарда, рекомендуется обратить внимание на репутацию, отзывы и условия, предлагаемые различными ломбардами. Также полезно обратиться за советом к знакомым или рекомендациям, чтобы выбрать надежный и ответственный ломбард.'
                }
                default_message = 'Извините, бот не может обработать этот запрос'
                if subcategory == 'Назад':
                    keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                    buttons = [types.KeyboardButton(text=key) for key in options2]
                    keyboard.add(*buttons)

                    bot.send_message(message.chat.id, 'Выберете категорию:', reply_markup=keyboard)
                else:
                    bot.reply_to(message, messages.get(subcategory, default_message))
        elif subcategory == 'Информация о СРО':
            keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
            buttons = [types.KeyboardButton(text=key) for key in questions_sro]
            keyboard.add(*buttons)
            bot.send_message(message.chat.id, 'Выберете вопрос:', reply_markup=keyboard)

            @bot.message_handler(func=lambda message: message.text in questions_sro)
            def handle_subcategory(message: telebot.types.Message):
                subcategory = message.text
                messages = {
                    'Что такое СРО?': 'СРО (саморегулируемая организация) – это организация, созданная в рамках определенной отрасли для саморегулирования и надзора за деятельностью своих членов. СРО устанавливают правила и стандарты, которым должны следовать ее члены.',
                    'Для чего создаются СРО?': 'СРО создаются для обеспечения надлежащего качества и безопасности услуг или работ в определенной отрасли. Они контролируют деятельность своих членов, разрабатывают общепринятые стандарты и регулируют сферу деятельности.',
                    'Кто может быть членом СРО?': 'Членами СРО могут быть юридические и физические лица, включая компании и специалистов, работающих в соответствующей отрасли. Членство в СРО обычно является добровольным, однако в некоторых случаях оно может быть обязательным.',
                    'Как стать членом СРО?': 'Процесс вступления в СРО может различаться в зависимости от конкретной организации и ее правил. Обычно требуется подать заявку, предоставить необходимые документы, выполнить определенные условия, такие как обучение или стажировка, и уплатить членские взносы.',
                    'Какие преимущества членства в СРО?': 'Членство в СРО может предоставлять ряд преимуществ. Это может включать доступ к информации и ресурсам, повышение доверия и репутации в отрасли, защиту прав и интересов членов, а также возможность повышения профессионального уровня.',
                    'Какова роль СРО в надзоре за своими членами?': 'СРО осуществляет надзор и контроль за деятельностью своих членов. Они могут проводить проверки, аудиты, разрабатывать правила и нормативы, а также рассматривать жалобы и принимать меры в отношении нарушителей.',
                    'Какие санкции могут быть наложены СРО на своих членов?': 'СРО могут применять различные санкции к своим членам в случае нарушения правил и стандартов. Это может включать штрафы, ограничения в деятельности, аннулирование членства или другие меры в соответствии с уставом организации.',
                    'Как получить информацию о СРО и их деятельности?': 'Для получения подробной информации о конкретном СРО можно обратиться на их официальные веб-сайты, изучить их устав и правила, а также проконсультироваться у представителей организации или других профессионалов в отрасли.'
                }
                default_message = 'Извините, бот не может обработать этот запрос'
                if subcategory == 'Назад':
                    keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                    buttons = [types.KeyboardButton(text=key) for key in options2]
                    keyboard.add(*buttons)

                    bot.send_message(message.chat.id, 'Выберете категорию:', reply_markup=keyboard)
                else:
                    bot.reply_to(message, messages.get(subcategory, default_message))
        elif subcategory == 'Меню':
            keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
            buttons = [types.KeyboardButton(text=key) for key in keys]
            keyboard.add(*buttons)

            bot.send_message(message.chat.id, 'Выберете категорию:', reply_markup=keyboard)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = '''Я чат-бот, который поможет Вам узнать актуальную информацию о микрофинансовых организациях. Здесь Вы сможете найти ответы на все вопросы об условиях займов и сбережений, процентных ставках, сроках и прочих услугах. Начнём?'''
    bot.reply_to(message, text)

    keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
    buttons = [types.KeyboardButton(text=key) for key in keys]
    keyboard.add(*buttons)

    bot.send_message(message.chat.id, 'Выберете категорию:', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text in keys)
def handle_category(message: telebot.types.Message):
    category = message.text
    if category == 'Контакты':
        menu = ['Меню']
        keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
        buttons = [types.KeyboardButton(text=key) for key in menu]
        keyboard.add(*buttons)

        @bot.message_handler(func=lambda message: message.text in 'Меню')
        def handle_subcategory(message: telebot.types.Message):
            subcategory = message.text
            if subcategory == 'Меню':
                keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                buttons = [types.KeyboardButton(text=key) for key in keys]
                keyboard.add(*buttons)
                bot.send_message(message.chat.id, 'Выберете категорию:', reply_markup=keyboard)

        bot.send_message(message.chat.id, 'Наши контактные данные: телефон - 123-456, email - example@example.com',
                         reply_markup=keyboard)

    if category == 'Сбережения':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
        buttons = [types.KeyboardButton(text=key) for key in yes_no]
        keyboard.add(*buttons)

        bot.send_message(message.chat.id, 'Принято ли решение о типе организации:', reply_markup=keyboard)

        @bot.message_handler(func=lambda message: message.text in 'Меню')
        def handle_subcategory(message: telebot.types.Message):
            subcategory = message.text
            if subcategory == 'Меню':
                keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                buttons = [types.KeyboardButton(text=key) for key in keys]
                keyboard.add(*buttons)

                bot.send_message(message.chat.id, 'Выберете категорию:', reply_markup=keyboard)

        @bot.message_handler(func=lambda message: message.text in yes_no)
        def handle_subcategory(message: telebot.types.Message):
            subcategory = message.text
            if subcategory == 'Да':
                keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                buttons = [types.KeyboardButton(text=key) for key in keys2]
                keyboard.add(*buttons)
                bot.send_message(message.chat.id, 'Выберете категорию:', reply_markup=keyboard)
            elif subcategory == 'Нет':
                keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                buttons = [types.KeyboardButton(text=key) for key in yes_no2]
                keyboard.add(*buttons)
                bot.send_message(message.chat.id, 'Хотите узнать больше про все типы организаций?',
                                 reply_markup=keyboard)

                @bot.message_handler(func=lambda message: message.text in yes_no2)
                def handle_subcategory(message: telebot.types.Message):
                    subcategory = message.text
                    if subcategory == 'Да, хочу':
                        keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                        buttons = [types.KeyboardButton(text=key) for key in options2]
                        keyboard.add(*buttons)
                        bot.send_message(message.chat.id, 'Выберете категорию:', reply_markup=keyboard)
                        faq()
                    elif subcategory == 'Нет, не хочу':
                        keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                        buttons = [types.KeyboardButton(text=key) for key in online_ofline]
                        keyboard.add(*buttons)
                        bot.send_message(message.chat.id,
                                         'Хотите онлайн? (Обратите внимание, что онлайн сбережение можно получить только в МФО от 1,5 млн рублей)',
                                         reply_markup=keyboard)

                        @bot.message_handler(func=lambda message: message.text in online_ofline)
                        def handle_subcategory(message: telebot.types.Message):
                            global online_bool
                            global type_org
                            subcategory = message.text
                            if subcategory == 'Онлайн':
                                online_bool = True
                                type_org.append("МФК")

                                bot.send_message(message.chat.id,
                                                 'На какую сумму хотите инвестировать?')
                                ans = {}

                                def handle_sum(message: telebot.types.Message):
                                    ans['sum'] = message.text
                                    bot.send_message(message.chat.id,
                                                     'На сколько дней хотите разместить деньги?')
                                    bot.register_next_step_handler(message, handle_period)

                                def handle_period(message: telebot.types.Message):
                                    ans['period'] = (message.text)
                                    bot.send_message(message.chat.id,
                                                     'Под какой процент хотите разместить деньги(от 0 до 1)?')
                                    bot.register_next_step_handler(message, handle_percent)

                                def handle_percent(message: telebot.types.Message):
                                    global type_org
                                    ans['percent'] = message.text
                                    bot.send_message(message.chat.id,
                                                     'Вот список подходящих Вам предложений по сбережениям: \n')
                                    for j in products:
                                        proc = float(ans['percent'])
                                        if j["product_type"] == "сбережения" and (
                                                (proc - 0.01 <= j["rate"])) and (j["term_min"]) <= int(
                                            ans['period']) <= j[
                                            "term_max"] and j["amount_min"] <= int(ans['sum']) <= j[
                                            "amount_max"] and ((j["method_reg"] == "офлайн/онлайн") or (
                                                j["method_reg"] == "онлайн" and online_bool) or (
                                                                       not online_bool and j[
                                                                   "method_reg"] == "офлайн")):
                                            id_org = j["id_org"]
                                            for i in organizations:
                                                if int(i["id"]) == int(id_org) and (
                                                        type_org == [] or i["organisation_type"] in type_org):
                                                    bot.send_message(message.chat.id,
                                                                     "Название компании: " + i["name_full"] +
                                                                     "\nПроцент: " + str(j["rate"]) +
                                                                     "\nАдрес: " + i[
                                                                         "location_reg"] + "\n Телефон: " +
                                                                     i["phone"] + "\nEmail: " + i["email"])

                                    type_org.clear()

                                    menu = ['Меню']
                                    keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                                    buttons = [types.KeyboardButton(text=key) for key in menu]
                                    keyboard.add(*buttons)

                                    @bot.message_handler(func=lambda message: message.text in 'Меню')
                                    def handle_subcategory(message: telebot.types.Message):
                                        subcategory = message.text
                                        if subcategory == 'Меню':
                                            keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                                            buttons = [types.KeyboardButton(text=key) for key in keys]
                                            keyboard.add(*buttons)
                                            bot.send_message(message.chat.id, 'Выберете категорию:',
                                                             reply_markup=keyboard)

                                bot.register_next_step_handler(message, handle_sum)

                            if subcategory == 'Офлайн':
                                online_bool = False
                                keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                                buttons = [types.KeyboardButton(text=key) for key in often]
                                keyboard.add(*buttons)
                                bot.send_message(message.chat.id, 'Как часто Вы пользуетесь сбережениями?',
                                                 reply_markup=keyboard)

                            @bot.message_handler(func=lambda message: message.text in often)
                            def handle_subcategory(message: telebot.types.Message):
                                subcategory = message.text
                                if subcategory == 'Редко':
                                    bot.send_message(message.chat.id,
                                                     'На какую сумму хотите инвестировать?')
                                    ans = {}

                                    def handle_sum(message: telebot.types.Message):
                                        ans['sum'] = message.text
                                        bot.send_message(message.chat.id,
                                                         'На сколько дней хотите разместить деньги?')
                                        bot.register_next_step_handler(message, handle_period)

                                    def handle_period(message: telebot.types.Message):
                                        ans['period'] = message.text
                                        bot.send_message(message.chat.id,
                                                         'Под какой процент хотите разместить деньги(от 0 до 1)?')
                                        bot.register_next_step_handler(message, handle_percent)

                                    def handle_percent(message: telebot.types.Message):
                                        global type_org
                                        ans['percent'] = message.text
                                        bot.send_message(message.chat.id,
                                                         'Вот список подходящих Вам предложений по сбережениям: \n')
                                        for j in products:
                                            proc = float(ans['percent'])
                                            if j["product_type"] == "сбережения" and (
                                                    (proc - 0.01 <= j["rate"])) and (
                                                    j["term_min"]) <= int(ans['period']) <= j[
                                                "term_max"] and j["amount_min"] <= int(ans['sum']) <= j[
                                                "amount_max"] and ((j["method_reg"] == "офлайн/онлайн") or (
                                                    j["method_reg"] == "онлайн" and online_bool) or (
                                                                           not online_bool and j[
                                                                       "method_reg"] == "офлайн")):
                                                id_org = j["id_org"]
                                                for i in organizations:
                                                    if int(i["id"]) == int(id_org) and (
                                                            type_org == [] or i["organisation_type"] in type_org):
                                                        bot.send_message(message.chat.id,
                                                                         "Название компании: " + i["name_full"] +
                                                                         "\nПроцент: " + str(j["rate"]) +
                                                                         "\nАдрес: " + i[
                                                                             "location_reg"] + "\n Телефон: " +
                                                                         i["phone"] + "\nEmail: " + i["email"])
                                        type_org.clear()

                                    bot.register_next_step_handler(message, handle_sum)
                                if subcategory == 'Регулярно':
                                    response2 = {'Нет, не подходит', 'Отлично'}
                                    keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                                    buttons = [types.KeyboardButton(text=key) for key in response2]
                                    keyboard.add(*buttons)
                                    bot.send_message(message.chat.id,
                                                     'Тогда рекомендуем стать Вам членом КПК, чтобы сделать сбережения в любой момент',
                                                     reply_markup=keyboard)

                                    @bot.message_handler(func=lambda message: message.text in response2)
                                    def handle_subcategory(message: telebot.types.Message):
                                        subcategory = message.text
                                        global type_org
                                        if subcategory == 'Отлично':
                                            type_org.append("КПК")
                                        bot.send_message(message.chat.id,
                                                         'На какую сумму хотите инвестировать?')
                                        ans = {}

                                        def handle_sum(message: telebot.types.Message):
                                            ans['sum'] = message.text
                                            bot.send_message(message.chat.id,
                                                             'На сколько дней хотите разместить деньги?')
                                            bot.register_next_step_handler(message, handle_period)

                                        def handle_period(message: telebot.types.Message):
                                            ans['period'] = message.text
                                            bot.send_message(message.chat.id,
                                                             'Под какой процент хотите разместить деньги(от 0 до 1)?')
                                            bot.register_next_step_handler(message, handle_percent)

                                        def handle_percent(message: telebot.types.Message):
                                            global type_org
                                            ans['percent'] = message.text
                                            bot.send_message(message.chat.id,
                                                             'Вот список подходящих Вам предложений по сбережениям: \n')
                                            for j in products:
                                                proc = float(ans['percent'])
                                                if j["product_type"] == "сбережения" and (
                                                        (proc - 0.01 <= j["rate"])) and (
                                                        j["term_min"]) <= int(ans['period']) <= j[
                                                    "term_max"] and j["amount_min"] <= int(ans['sum']) <= j[
                                                    "amount_max"] and ((j["method_reg"] == "офлайн/онлайн") or (
                                                        j["method_reg"] == "онлайн" and online_bool) or (
                                                                               not online_bool and j[
                                                                           "method_reg"] == "офлайн")):
                                                    id_org = j["id_org"]
                                                    for i in organizations:
                                                        if int(i["id"]) == int(id_org) and (
                                                                type_org == [] or i["organisation_type"] in type_org):
                                                            bot.send_message(message.chat.id,
                                                                             "Название компании: " + i["name_full"] +
                                                                             "\nПроцент: " + str(j["rate"]) +
                                                                             "\nАдрес: " + i[
                                                                                 "location_reg"] + "\n Телефон: " +
                                                                             i["phone"] + "\nEmail: " + i["email"])
                                            type_org.clear()

                                        bot.register_next_step_handler(message, handle_sum)

        @bot.message_handler(func=lambda message: message.text in keys2)
        def handle_subcategory1(message: telebot.types.Message):
            subcategory = message.text

            options = {'ИНН', 'ОГРН', 'Название', 'Меню'}
            if subcategory == 'Меню':
                keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                buttons = [types.KeyboardButton(text=key) for key in keys]
                keyboard.add(*buttons)

                bot.send_message(message.chat.id, 'Выберете категорию:', reply_markup=keyboard)
            elif subcategory in ['МФК', 'КПК', 'СКПК', 'Ломбард']:
                keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                buttons = [types.KeyboardButton(text=key) for key in options]
                keyboard.add(*buttons)

                bot.send_message(message.chat.id, 'По какому признаку вы хотите выбрать организацию:',
                                 reply_markup=keyboard)

                @bot.message_handler(func=lambda message: message.text in options)
                def handle_subcategory2(message: telebot.types.Message):
                    subcategory = message.text
                    if subcategory == 'ИНН':
                        bot.send_message(message.chat.id, 'Введите ИНН:')

                        @bot.message_handler(func=lambda message: True)
                        def handle_message(message):
                            query = message.text
                            for i in organizations:
                                if i["inn"] == int(query):
                                    org_id = i["id"]
                                    for j in products:
                                        if int(j['id_org']) == int(org_id) and j["product_type"] == "сбережения":
                                            bot.send_message(message.chat.id, "Название компании: " + i["name_full"] +
                                            "\nМинимальная сумма: " + str(j["amount_min"]) + "\nМаксимальная сумма: " +
                                            str(j["amount_max"]) + "\nМинимальный срок(в днях): " + str(j["term_min"]) +
                                            "\nМаксимальная сумма: " + str(j["term_max"]) + "\nСтавка: " + str(j["rate"])
                                            , reply_markup=keyboard)

                    elif subcategory == 'ОГРН':
                        bot.send_message(message.chat.id, 'Введите ОГРН:')

                        @bot.message_handler(func=lambda message: True)
                        def handle_message(message):
                            query = message.text
                            for i in organizations:
                                if i["ogrn"] == int(query):
                                    org_id = i["id"]
                                    for j in products:
                                        if int(j['id_org']) == int(org_id) and j["product_type"] == "сбережения":
                                            bot.send_message(message.chat.id, "Название компании: " + i["name_full"] +
                                                             "\nМинимальная сумма: " + str(
                                                j["amount_min"]) + "\nМаксимальная сумма: " +
                                                             str(j[
                                                                     "amount_max"]) + "\nМинимальный срок(в днях): " + str(
                                                j["term_min"]) +
                                                             "\nМаксимальная сумма: " + str(
                                                j["term_max"]) + "\nСтавка: " + str(j["rate"])
                                                             , reply_markup=keyboard)

                    elif subcategory == 'Название':
                        bot.send_message(message.chat.id, 'Введите Название:')

                        @bot.message_handler(func=lambda message: True)
                        def handle_message(message):
                            query = message.text
                            for i in organizations:
                                if i["name_short"] == (query) or i["name_full"] == (query) or i["brand_name"] == (
                                        query):
                                    org_id = i["id"]
                                    for j in products:
                                        if int(j['id_org']) == int(org_id) and j["product_type"] == "сбережения":
                                            bot.send_message(message.chat.id, "Название компании: " + i["name_full"] +
                                                             "\nМинимальная сумма: " + str(
                                                j["amount_min"]) + "\nМаксимальная сумма: " +
                                                             str(j[
                                                                     "amount_max"]) + "\nМинимальный срок(в днях): " + str(
                                                j["term_min"]) +
                                                             "\nМаксимальная сумма: " + str(
                                                j["term_max"]) + "\nСтавка: " + str(j["rate"])
                                                             , reply_markup=keyboard)

    if category == 'Заем':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
        buttons = [types.KeyboardButton(text=key) for key in yes_no3]
        keyboard.add(*buttons)

        bot.send_message(message.chat.id, 'Принято ли решение о типе организации:', reply_markup=keyboard)

        @bot.message_handler(func=lambda message: message.text in 'Меню')
        def handle_subcategory(message: telebot.types.Message):
            subcategory = message.text
            if subcategory == 'Меню':
                keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                buttons = [types.KeyboardButton(text=key) for key in keys]
                keyboard.add(*buttons)

                bot.send_message(message.chat.id, 'Выберете категорию:', reply_markup=keyboard)

        @bot.message_handler(func=lambda message: message.text in yes_no3)
        def handle_subcategory(message: telebot.types.Message):
            subcategory = message.text
            if subcategory == 'Да, принято':
                keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                buttons = [types.KeyboardButton(text=key) for key in keys3]
                keyboard.add(*buttons)
                bot.send_message(message.chat.id, 'Выберете категорию:', reply_markup=keyboard)
            if subcategory == 'Нет, не принято':
                keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                buttons = [types.KeyboardButton(text=key) for key in yes_no4]
                keyboard.add(*buttons)
                bot.send_message(message.chat.id, 'Хотите узнать больше про все типы организаций?',
                                 reply_markup=keyboard)

                @bot.message_handler(func=lambda message: message.text in yes_no4)
                def handle_subcategory(message: telebot.types.Message):
                    subcategory = message.text
                    if subcategory == 'Хочу':
                        keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                        buttons = [types.KeyboardButton(text=key) for key in options2]
                        keyboard.add(*buttons)
                        bot.send_message(message.chat.id, 'Выберете категорию:', reply_markup=keyboard)
                        faq()
                    if subcategory == 'Не хочу':
                        keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                        buttons = [types.KeyboardButton(text=key) for key in online_ofline2]
                        keyboard.add(*buttons)
                        bot.send_message(message.chat.id,
                                         'Хотите онлайн? (Обратите внимание, что онлайн сбережение можно получить только в МФО от 1,5 млн рублей)',
                                         reply_markup=keyboard)

                        @bot.message_handler(func=lambda message: message.text in online_ofline2)
                        def handle_subcategory(message: telebot.types.Message):
                            subcategory = message.text
                            global online_bool
                            global type_org
                            if subcategory == 'Хочу онлайн':
                                online_bool = True
                                type_org.append("МФК")
                                type_org.append("МКК")

                                bot.send_message(message.chat.id,
                                                 'На какую сумму хотите получить займ?')
                                ans = {}

                                def handle_sum(message: telebot.types.Message):
                                    ans['sum'] = message.text
                                    bot.send_message(message.chat.id,
                                                     'На сколько дней хотите получить займ?')
                                    bot.register_next_step_handler(message, handle_period)

                                def handle_period(message: telebot.types.Message):
                                    ans['period'] = message.text
                                    bot.send_message(message.chat.id,
                                                     'Под какой процент хотите получить займ(от 0 до 1)?')
                                    bot.register_next_step_handler(message, handle_percent)

                                def handle_percent(message: telebot.types.Message):
                                    global type_org
                                    ans['percent'] = message.text
                                    bot.send_message(message.chat.id,
                                                     'Вот список подходящих Вам предложений по займам: \n')
                                    for j in products:
                                        proc = float(ans['percent'])
                                        if j["product_type"] == "заем" and (
                                                (j["rate"]) <= proc + 0.01) and (j["term_min"]) <= int(
                                            ans['period']) <= j[
                                            "term_max"] and j["amount_min"] <= int(ans['sum']) <= j[
                                            "amount_max"] and ((j["method_reg"] == "офлайн/онлайн") or (
                                                j["method_reg"] == "онлайн" and online_bool) or (
                                                                       not online_bool and j[
                                                                   "method_reg"] == "офлайн")):
                                            id_org = j["id_org"]
                                            for i in organizations:
                                                if int(i["id"]) == int(id_org) and (
                                                        type_org == [] or i["organisation_type"] in type_org):
                                                    bot.send_message(message.chat.id,
                                                                     "Название компании: " + i["name_full"] +
                                                                     "\nПроцент: " + str(j["rate"]) +
                                                                     "\nАдрес: " + i[
                                                                         "location_reg"] + "\n Телефон: " +
                                                                     i["phone"] + "\nEmail: " + i["email"])
                                    type_org.clear()

                                bot.register_next_step_handler(message, handle_sum)

                            if subcategory == 'Хочу офлайн':
                                online_bool = False
                                keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                                buttons = [types.KeyboardButton(text=key) for key in often2]
                                keyboard.add(*buttons)
                                bot.send_message(message.chat.id, 'Как часто Вы пользуетесь займами?',
                                                 reply_markup=keyboard)

                        @bot.message_handler(func=lambda message: message.text in often2)
                        def handle_subcategory(message: telebot.types.Message):
                            subcategory = message.text
                            if subcategory == 'Часто':
                                options = {'Нет необходимости', 'Давайте'}
                                keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                                buttons = [types.KeyboardButton(text=key) for key in options]
                                keyboard.add(*buttons)
                                bot.send_message(message.chat.id,
                                                 'Тогда рекомендуем Вам стать членом КПК, чтобы брать займы в любой момент',
                                                 reply_markup=keyboard)

                                @bot.message_handler(func=lambda message: message.text in options)
                                def handle_subcategory(message: telebot.types.Message):
                                    global type_org
                                    subcategory = message.text
                                    if subcategory == 'Давайте':
                                        type_org.append("КПК")
                                    bot.send_message(message.chat.id,
                                                     'На какую сумму хотите получить займ?')
                                    ans = {}

                                    def handle_sum(message: telebot.types.Message):
                                        ans['sum'] = message.text
                                        bot.send_message(message.chat.id,
                                                         'На сколько дней хотите получить займ?')
                                        bot.register_next_step_handler(message, handle_period)

                                    def handle_period(message: telebot.types.Message):
                                        ans['period'] = message.text
                                        bot.send_message(message.chat.id,
                                                         'Под какой процент хотите получить займ(от 0 до 1)?')
                                        bot.register_next_step_handler(message, handle_percent)

                                    def handle_percent(message: telebot.types.Message):
                                        global type_org
                                        ans['percent'] = message.text
                                        bot.send_message(message.chat.id,
                                                         'Вот список подходящих Вам предложений по заемам: \n')
                                        for j in products:
                                            proc = float(ans['percent'])
                                            if j["product_type"] == "займ" and (
                                                    (j["rate"]) <= proc + 0.01) and (
                                                    j["term_min"]) <= int(ans['period']) <= j[
                                                "term_max"] and j["amount_min"] <= int(ans['sum']) <= j[
                                                "amount_max"] and ((j["method_reg"] == "офлайн/онлайн") or (
                                                    j["method_reg"] == "онлайн" and online_bool) or (
                                                                           not online_bool and j[
                                                                       "method_reg"] == "офлайн")):
                                                id_org = j["id_org"]
                                                for i in organizations:
                                                    if int(i["id"]) == int(id_org) and (
                                                            type_org == [] or i["organisation_type"] in type_org):
                                                        bot.send_message(message.chat.id,
                                                                         "Название компании: " + i["name_full"] +
                                                                         "\nПроцент: " + str(j["rate"]) +
                                                                         "\nАдрес: " + i[
                                                                             "location_reg"] + "\n Телефон: " +
                                                                         i["phone"] + "\nEmail: " + i["email"])
                                        type_org.clear()

                                    bot.register_next_step_handler(message, handle_sum)

                            if subcategory == 'Иногда':
                                bot.send_message(message.chat.id,
                                                 'На какую сумму хотите получить займ?')
                                ans = {}

                                def handle_sum(message: telebot.types.Message):
                                    ans['sum'] = message.text
                                    bot.send_message(message.chat.id,
                                                     'На какой срок хотите получить займ?')
                                    bot.register_next_step_handler(message, handle_period)

                                def handle_period(message: telebot.types.Message):
                                    ans['period'] = message.text
                                    bot.send_message(message.chat.id,
                                                     'Под какой процент хотите получить займ(от 0 до 1)?')
                                    bot.register_next_step_handler(message, handle_percent)

                                def handle_percent(message: telebot.types.Message):
                                    global type_org
                                    ans['percent'] = message.text
                                    bot.send_message(message.chat.id,
                                                     'Вот список подходящих Вам предложений по заемам: \n')
                                    for j in products:
                                        proc = float(ans['percent'])
                                        if j["product_type"] == "заем" and (
                                                (j["rate"]) <= proc + 0.01) and (
                                                j["term_min"]) <= int(
                                            ans['period']) <= j["term_max"] and j["amount_min"] <= int(
                                            ans['sum']) <= j["amount_max"] and (
                                                (j["method_reg"] == "офлайн/онлайн") or (
                                                j["method_reg"] == "онлайн" and online_bool) or (
                                                        not online_bool and j[
                                                    "method_reg"] == "офлайн")):
                                            id_org = j["id_org"]
                                            for i in organizations:
                                                if int(i["id"]) == int(id_org) and (
                                                        type_org == [] or i["organisation_type"] in type_org):
                                                    bot.send_message(message.chat.id,
                                                                     "Название компании: " + i["name_full"] +
                                                                     "\nПроцент: " + str(j["rate"]) +
                                                                     "\nАдрес: " + i[
                                                                         "location_reg"] + "\n Телефон: " +
                                                                     i["phone"] + "\nEmail: " + i["email"])
                                    type_org.clear()

                                bot.register_next_step_handler(message, handle_sum)

        @bot.message_handler(func=lambda message: message.text in keys3)
        def handle_subcategory1(message: telebot.types.Message):
            subcategory = message.text

            options = {'ИНН', 'ОГРН', 'Название', 'Меню'}
            if subcategory == 'Меню':
                keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                buttons = [types.KeyboardButton(text=key) for key in keys]
                keyboard.add(*buttons)

                bot.send_message(message.chat.id, 'Выберете категорию:', reply_markup=keyboard)
            elif subcategory in ['Хочу взять заем в МФК', 'Хочу взять заем в МКК', 'Хочу взять заем в КПК',
                                 'Хочу взять заем в СКПК', 'Хочу взять заем в Ломбарде']:
                keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
                buttons = [types.KeyboardButton(text=key) for key in options]
                keyboard.add(*buttons)

                bot.send_message(message.chat.id, 'По какому признаку вы хотите выбрать организацию:',
                                 reply_markup=keyboard)

                @bot.message_handler(func=lambda message: message.text in options)
                def handle_subcategory2(message: telebot.types.Message):
                    subcategory = message.text
                    if subcategory == 'ИНН':
                        bot.send_message(message.chat.id, 'Введите ИНН:')

                        @bot.message_handler(func=lambda message: True)
                        def handle_message(message):
                            query = message.text
                            for i in organizations:
                                if i["inn"] == int(query):
                                    org_id = i["id"]
                                    for j in products:
                                        if int(j['id_org']) == int(org_id) and j["product_type"] == "заем":
                                            bot.send_message(message.chat.id, "Название компании: " + i["name_full"] +
                                                             "\nМинимальная сумма: " + str(
                                                j["amount_min"]) + "\nМаксимальная сумма: " +
                                                             str(j[
                                                                     "amount_max"]) + "\nМинимальный срок(в днях): " + str(
                                                j["term_min"]) +
                                                             "\nМаксимальная сумма: " + str(
                                                j["term_max"]) + "\nСтавка: " + str(j["rate"])
                                                             , reply_markup=keyboard)

                    elif subcategory == 'ОГРН':
                        bot.send_message(message.chat.id, 'Введите ОГРН:')

                        @bot.message_handler(func=lambda message: True)
                        def handle_message(message):
                            query = message.text
                            for i in organizations:
                                if i["ogrn"] == int(query):
                                    org_id = i["id"]
                                    for j in products:
                                        if int(j['id_org']) == int(org_id) and j["product_type"] == "заем":
                                            bot.send_message(message.chat.id, "Название компании: " + i["name_full"] +
                                                             "\nМинимальная сумма: " + str(
                                                j["amount_min"]) + "\nМаксимальная сумма: " +
                                                             str(j[
                                                                     "amount_max"]) + "\nМинимальный срок(в днях): " + str(
                                                j["term_min"]) +
                                                             "\nМаксимальная сумма: " + str(
                                                j["term_max"]) + "\nСтавка: " + str(j["rate"])
                                                             , reply_markup=keyboard)

                    elif subcategory == 'Название':
                        bot.send_message(message.chat.id, 'Введите Название:')

                        @bot.message_handler(func=lambda message: True)
                        def handle_message(message):
                            query = message.text
                            for i in organizations:
                                if i["name_short"] == (query) or i["name_full"] == (query) or i["brand_name"] == (
                                        query):
                                    org_id = i["id"]
                                    for j in products:
                                        if int(j['id_org']) == int(org_id) and j["product_type"] == "заем":
                                            bot.send_message(message.chat.id, "Название компании: " + i["name_full"] +
                                                             "\nМинимальная сумма: " + str(
                                                j["amount_min"]) + "\nМаксимальная сумма: " +
                                                             str(j[
                                                                     "amount_max"]) + "\nМинимальный срок(в днях): " + str(
                                                j["term_min"]) +
                                                             "\nМаксимальная сумма: " + str(
                                                j["term_max"]) + "\nСтавка: " + str(j["rate"])
                                                             , reply_markup=keyboard)

    if category == 'FAQ':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
        buttons = [types.KeyboardButton(text=key) for key in options2]
        keyboard.add(*buttons)
        bot.send_message(message.chat.id, 'Выберете категорию:', reply_markup=keyboard)
        faq()

    if category == 'Проверка своей кредитной истории':
        text = 'Вы можете воспользоваться услугами БКИ: https://nbki.ru/'
        bot.reply_to(message, text)

    if category == 'Проверка надежности организации':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
        buttons = [types.KeyboardButton(text=key) for key in options]
        keyboard.add(*buttons)
        bot.send_message(message.chat.id, 'Выберете категорию:', reply_markup=keyboard)

        @bot.message_handler(func=lambda message: message.text in options)
        def handle_subcategory2(message: telebot.types.Message):
            subcategory = message.text
            if subcategory == 'ИНН':
                bot.send_message(message.chat.id, 'Введите ИНН:')

                @bot.message_handler(func=lambda message: True)
                def handle_message(message):
                    query = message.text
                    for i in organizations:
                        if i["inn"] == int(query):
                            bot.send_message(message.chat.id, "Название компании: " + i["name_full"] +
                                             "\nРейтинг: " + str(i["rating"]), reply_markup=keyboard)

            elif subcategory == 'ОГРН':
                bot.send_message(message.chat.id, 'Введите ОГРН:')

                @bot.message_handler(func=lambda message: True)
                def handle_message(message):
                    query = message.text
                    for i in organizations:
                        if i["ogrn"] == int(query):
                            bot.send_message(message.chat.id, "Название компании: " + i["name_full"] +
                                             "\nРейтинг: " + str(i["rating"]), reply_markup=keyboard)

            elif subcategory == 'Название':
                bot.send_message(message.chat.id, 'Введите Название:')

                @bot.message_handler(func=lambda message: True)
                def handle_message(message):
                    query = message.text
                    for i in organizations:
                        if i["name_short"] == (query) or i["name_full"] == (query) or i["brand_name"] == (
                                query):
                            bot.send_message(message.chat.id, "Название компании: " + i["name_full"] +
                                             "\nРейтинг: " + str(i["rating"]), reply_markup=keyboard)


bot.polling()
