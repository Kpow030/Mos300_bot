import telebot
import logging


from telebot import types
from All import (links, registered_users)
from All import (open_random_link, send_post, generate_share_links, handle_message,
                 send_telegram_message, gather_feedback, try_again)






bot = telebot.TeleBot("token")

TOKEN = "Token"

logging.basicConfig(filename='bot_errors.log', level=logging.ERROR)


def log_error(error_msg):
    logging.error(error_msg)





@bot.message_handler(commands=["start", "help"])  # Начало викторины
def welcome(message):
    bot.send_message(message.chat.id, "👋 Привет! Я бот 'Московского Зоопарка'")
    if message.from_user.id in registered_users:
        bot.send_message(message.chat.id, "Вы уже зарегистрированы.")
    else:
        registered_users[message.from_user.id] = {'username': message.from_user.username, 'id': message.from_user.id}
        bot.send_message(message.chat.id, "Вы успешно зарегистрированы.")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mrk = types.KeyboardButton("🏁Хочу участвовать")
    mrk1 = types.KeyboardButton("⛔Не хочу участвовать")
    markup.add(mrk, mrk1)
    bot.send_message(message.chat.id, "Вас привлекает идея участия в увлекательной викторине? "
                                      " Это всего несколько вопросов, которые помогут нам лучше узнать вас. "
                                      " В зависимости от ваших ответов, я представлю вам некоторые виды животных, "
                                      " которым сегодня требуется наша совместная помощь 🆘📕. "
                                      " Это замечательная возможность не только узнать больше о нашем богатом "
                                      " и многообразном животном мире, но и внести свой вклад в его защиту. "
                                      " Желать принять участие?",
                                        reply_markup=markup)

    with open('F:\Бот\Moscow3оо\images\Logo.jpg', "rb")  as photo:
        bot.send_photo(message.chat.id, photo)




@bot.message_handler(commands=['registered'])
def show_registered_users(message):
    # Показываем список зарегистрированных пользователей
    users = "\n".join([f"{user['id']}: @{user['username']}" for user in registered_users.values()])
    bot.send_message(message.chat.id, f"Зарегистрированные пользователи:\n{users}")




@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '🏁Хочу участвовать':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Выводятся после согласия
        mar = types.KeyboardButton('Воздух 💨')
        mar1 = types.KeyboardButton('Земля 🌎')
        mar2 = types.KeyboardButton('Огонь 🔥')
        mar3 = types.KeyboardButton('Вода 💧')
        mar4 = types.KeyboardButton('Назад в меню')
        markup.add(mar, mar1, mar2, mar3, mar4)
        bot.send_message(message.from_user.id, 'Выберите стихию, соответствующую вашему духу: '
                                               'вода 💧 (гибкость), воздух 💨 (свобода), '
                                               'земля 🌍 (стабильность) или огонь 🔥 (страсть)', reply_markup=markup)



    elif message.text == 'Назад в меню':
        handle_message(message)


    elif message.text == '🏁Хочу участвовать':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Выводятся после согласия
        mar = types.KeyboardButton('Воздух 💨')
        mar1 = types.KeyboardButton('Земля 🌎')
        mar2 = types.KeyboardButton('Огонь 🔥')
        mar3 = types.KeyboardButton('Вода 💧')
        markup.add(mar, mar1, mar2, mar3)
        bot.send_message(message.from_user.id,  'Выберите стихию, соответствующую вашему духу: '                    
                                               'вода 💧 (гибкость), воздух 💨 (свобода), '
                                               'земля 🌍 (стабильность) или огонь 🔥 (страсть)', reply_markup=markup)


    elif message.text == '⛔Не хочу участвовать':
        link = open_random_link(links)
        response = f"Очень жаль, что вы отказываетесь. Ведь я нуждаюсь в вашей помощи 🆘"
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Открыть ссылку", url=link)
        markup.add(btn1)
        bot.send_message(message.from_user.id, response, reply_markup=markup)



    elif message.text == 'Воздух 💨':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Начинаем собирать информацию
        mar = types.KeyboardButton('Летать 🛸')
        mar1 = types.KeyboardButton('Гулять 👣')
        mar2 = types.KeyboardButton('Ночь 🌑')
        mar3 = types.KeyboardButton('Осень ☔')
        mar4 = types.KeyboardButton('Лето 🌞')
        mar5 = types.KeyboardButton('Назад в меню')
        markup.add(mar, mar1, mar2, mar3, mar4, mar5)
        bot.send_message(message.from_user.id, "Отлично, выберите что вам нравится из перечисленного",
                                                reply_markup=markup)



    elif message.text == 'Назад в меню':
        bot.send_message(message.chat.id,
                         "Иногда нужно сделать 'Шаг назад что бы сделать два шага вперед'")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mrk = types.KeyboardButton("Да конечно")
        mrk1 = types.KeyboardButton("Нет, я передумал")
        markup.add(mrk, mrk1)
        bot.send_message(message.from_user.id,
                         "Давайте продолжим наш опрос?", reply_markup=markup)


    elif message.text == 'Летать 🛸':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Происходит выбор где хотел бы "летать" наш пользователь
        mar = types.KeyboardButton('Летать в горах 🦅')
        mar1 = types.KeyboardButton('Летать в тропиках 🦜')
        mar2 = types.KeyboardButton('Летать над рекой 🦩')
        mar3 = types.KeyboardButton('Летать в лесу 🦉')
        mar4 = types.KeyboardButton('Назад в меню')
        mar5 = types.KeyboardButton('Оставить отзыв')
        retry_button = types.KeyboardButton("Попробовать еще раз")
        markup.add(retry_button)
        markup.add(mar, mar1, mar2, mar3, mar4, mar5)
        bot.send_message(message.from_user.id,
                                            "Отлично! Мы уже на шаг ближе к знакомству с одним из наших "
                                            " удивительных обитателей. Но прежде, давайте выберем место, "
                                            " где вы бы хотели оказаться. Ваш выбор поможет нам лучше понять "
                                            " ваши предпочтения и подобрать для вас идеального 'питомца'. "
                                            " Ведь каждое место на нашей планете уникально "
                                            " и обладает своей собственной магией и очарованием. "
                                            " Где бы вы хотели оказаться?",
                                                 reply_markup=markup)


    elif message.text == 'Назад в меню':
        handle_message(message)


    elif message.text == 'Оставить отзыв':
        bot.send_message(message.from_user.id, "Пожалуйста, напишите свой отзыв:")
        bot.register_next_step_handler(message, gather_feedback)


    elif message.text == 'Летать в горах 🦅':
        user_id = message.from_user.id
        markup = types.InlineKeyboardMarkup()
        quiz_result = ("Поздравляю вас! Ваша уникальность и способность достигать высоких целей "
                       " напоминают мне о снежном грифе, величественной птице Гималаев. "
                       " Ваша способность подниматься высоко, ваша устойчивость и ваше уникальное видение мира "
                       " делают вас по-настоящему особенным, как этот удивительный обитатель высоких гор. "
                       " Пусть снежный гриф будет вашим символом устремленности к вершинам и бесстрашия, "
                       " и пусть он всегда вдохновляет вас на новые достижения. "
                       " Поздравляю вас с этим уникальным сочетанием качеств и желаю, "
                       " чтобы ваша жизнь была полна великих достижений! 🦅!!!")
        employee_id = ID  
        send_telegram_message(employee_id, f"Пользователь {user_id} успешно прошел викторину")
        image_path = 'F:\Бот\Moscow3оо\images\Grif.jpg'
        send_post(bot, message, image_path, quiz_result)
        facebook_share_link, vk_share_link = generate_share_links()
        btn1 = types.InlineKeyboardButton(text="Снежный Гриф 🦅" , url='https://moscowzoo.ru/animals/sokoloobraznye/grif/?sphrase_id=737599')
        btn2 = types.InlineKeyboardButton(text="Взять под опеку ❕", url='https://moscowzoo.ru/my-zoo/become-a-guardian/')
        btn_facebook = types.InlineKeyboardButton(" 🔲Поделиться в Facebook🔲", url=facebook_share_link)
        btn_vk = types.InlineKeyboardButton("🔲Поделиться в VK🔲", url=vk_share_link)
        markup.add(btn_facebook, btn1, btn2, btn_vk)
        bot.send_message(message.from_user.id, "Нажмите на кнопку 🔲, чтобы поделиться своим результатом или "
                                               " узнать больше о выбранном вами животном. "
                                               " Ведь каждое из них уникально и заслуживает нашего внимания."
                                               " Но помните, наши 'Братья меньшие' ℹ️ не всегда могут справиться "
                                               " без нашей помощи. Они нуждаются в защите и заботе, "
                                               " и каждый из нас может сделать свой вклад. 🆘"
                                               " Если вы чувствуете, что готовы подарить часть своего времени и любви "
                                               " этим удивительным созданиям, рассмотрите возможность взять под опеку "
                                               " 'ваше животное'. Ваша поддержка может сделать мир лучше для них."
                                               " Спасибо, что приняли участие в нашей викторине "
                                               " и проявили интерес к животному миру. Вместе мы можем сделать больше! ",
                                               reply_markup=markup)



    elif message.text == 'Попробовать еще раз':
        try_again(message)


    elif message.text == 'Оставить отзыв':
        bot.send_message(message.from_user.id, "Пожалуйста, напишите свой отзыв:")
        bot.register_next_step_handler(message, gather_feedback)


    elif message.text == 'Летать в тропиках 🦜':
        user_id = message.from_user.id
        markup = types.InlineKeyboardMarkup()
        quiz_result = ("Поздравляем, вы - настоящий Солдатский Ара! 🎉 "
                       " Этот результат показывает, что у вас есть яркая индивидуальность и "
                       " способность привлекать внимание окружающих, "
                       " словно красочный попугайчик. Ваша уникальность непременно вызывает восхищение!")
        employee_id = id  
        send_telegram_message(employee_id, f"Пользователь {user_id} успешно прошел викторину")
        image_path = 'F:\Бот\Moscow3оо\images\Ara.jpg'
        send_post(bot, message, image_path, quiz_result)
        facebook_share_link, vk_share_link = generate_share_links()
        btn1 = types.InlineKeyboardButton(text="Солдатский Ара 🦜",
                                          url='https://moscowzoo.ru/animals/popugaeobraznye/malyy-soldatskiy-ara/?sphrase_id=737595')
        btn2 = types.InlineKeyboardButton(text="Взять под опеку ❕", url='https://moscowzoo.ru/my-zoo/become-a-guardian/')
        btn_facebook = types.InlineKeyboardButton(" 🔲Поделиться в Facebook🔲", url=facebook_share_link)
        btn_vk = types.InlineKeyboardButton("🔲Поделиться в VK🔲", url=vk_share_link)
        markup.add(btn_facebook, btn1, btn2, btn_vk)
        bot.send_message(message.from_user.id, "Нажмите на кнопку 🔲, чтобы поделиться своим результатом или "
                                               " узнать больше о выбранном вами животном. "
                                               " Ведь каждое из них уникально и заслуживает нашего внимания."
                                               " Но помните, наши 'Братья меньшие' ℹ️ не всегда могут справиться "
                                               " без нашей помощи. Они нуждаются в защите и заботе, "
                                               " и каждый из нас может сделать свой вклад. 🆘"
                                               " Если вы чувствуете, что готовы подарить часть своего времени и любви "
                                               " этим удивительным созданиям, рассмотрите возможность взять под опеку "
                                               " 'ваше животное'. Ваша поддержка может сделать мир лучше для них."
                                               " Спасибо, что приняли участие в нашей викторине "
                                               " и проявили интерес к животному миру. Вместе мы можем сделать больше! ",
                                               reply_markup=markup)


    elif message.text == 'Попробовать еще раз':
        try_again(message)


    elif message.text == 'Оставить отзыв':
        bot.send_message(message.from_user.id, "Пожалуйста, напишите свой отзыв:")
        bot.register_next_step_handler(message, gather_feedback)


    elif message.text == 'Осень ☔':
        user_id = message.from_user.id
        markup = types.InlineKeyboardMarkup()
        quiz_result = ("Поздравляем! Вам отлично подходит Краснощёкий ибис! 🌟 "
                       " Это свидетельствует о вашей изысканной натуре и великолепной внешности. "
                       " Краснощёкий ибис - это символ прекрасной грации и изысканности, "
                       " и вам удается нести эти качества в себе."
                       " Поздравляем с таким выдающимся результатом !")
        employee_id = id  # Здесь  ID Telegram сотрудника зоопарка
        send_telegram_message(employee_id, f"Пользователь {user_id} успешно прошел викторину")
        image_path = 'F:\Бот\Moscow3оо\images\lesnoi ibis.jpg'
        send_post(bot, message, image_path, quiz_result)
        facebook_share_link, vk_share_link = generate_share_links()
        btn1 = types.InlineKeyboardButton(text="КРАСНОЩЕКИЙ ИБИС",
                                          url='https://moscowzoo.ru/animals/aistoobraznye/krasnoshchekiy-ibis/?sphrase_id=741329')
        btn2 = types.InlineKeyboardButton(text="Взять под опеку ❕", url='https://moscowzoo.ru/my-zoo/become-a-guardian/')
        btn_facebook = types.InlineKeyboardButton(" 🔲Поделиться в Facebook🔲", url=facebook_share_link)
        btn_vk = types.InlineKeyboardButton("🔲Поделиться в VK🔲", url=vk_share_link)
        markup.add(btn_facebook, btn1, btn2, btn_vk)
        bot.send_message(message.from_user.id, "Нажмите на кнопку 🔲, чтобы поделиться своим результатом или "
                                               " узнать больше о выбранном вами животном. "
                                               " Ведь каждое из них уникально и заслуживает нашего внимания."
                                               " Но помните, наши 'Братья меньшие' ℹ️ не всегда могут справиться "
                                               " без нашей помощи. Они нуждаются в защите и заботе, "
                                               " и каждый из нас может сделать свой вклад. 🆘"
                                               " Если вы чувствуете, что готовы подарить часть своего времени и любви "
                                               " этим удивительным созданиям, рассмотрите возможность взять под опеку "
                                               " 'ваше животное'. Ваша поддержка может сделать мир лучше для них."
                                               " Спасибо, что приняли участие в нашей викторине "
                                               " и проявили интерес к животному миру. Вместе мы можем сделать больше! ",
                                               reply_markup=markup)


    elif message.text == 'Попробовать еще раз':
        try_again(message)


    elif message.text == 'Оставить отзыв':
        bot.send_message(message.from_user.id, "Пожалуйста, напишите свой отзыв:")
        bot.register_next_step_handler(message, gather_feedback)


    elif message.text == 'Летать в лесу 🦉':
        user_id = message.from_user.id
        markup = types.InlineKeyboardMarkup()
        quiz_result = ("Поздравляю! Ваш результат - Длиннохвостая неясыть! 🌟 "
                       " Ваше обаяние и таинственность делают вас похожими на эту загадочную птицу. "
                       " Вас привлекает загадки и неизведанные территории, "
                       " и вы обладаете уникальным обонянием для отыскания ответов. "
                       " С вами всегда интересно и захватывающе! !!!")
        employee_id = id  # Здесь  ID Telegram сотрудника зоопарка
        send_telegram_message(employee_id, f"Пользователь {user_id} успешно прошел викторину")
        image_path = 'F:\Бот\Moscow3оо\images\easit.jpg'
        send_post(bot, message, image_path, quiz_result)
        facebook_share_link, vk_share_link = generate_share_links()
        btn1 = types.InlineKeyboardButton(text="Длиннохвостая неясыть 🦉",
                                          url='https://moscowzoo.ru/animals/sovoobraznye/dlinnokhvostaya-neyasyt/?sphrase_id=737598')
        btn2 = types.InlineKeyboardButton(text="Взять под опеку ❕", url='https://moscowzoo.ru/my-zoo/become-a-guardian/')
        btn_facebook = types.InlineKeyboardButton(" 🔲Поделиться в Facebook🔲", url=facebook_share_link)
        btn_vk = types.InlineKeyboardButton("🔲Поделиться в VK🔲", url=vk_share_link)
        markup.add(btn_facebook, btn1, btn2, btn_vk)
        bot.send_message(message.from_user.id, "Нажмите на кнопку 🔲, чтобы поделиться своим результатом или "
                                               " узнать больше о выбранном вами животном. "
                                               " Ведь каждое из них уникально и заслуживает нашего внимания."
                                               " Но помните, наши 'Братья меньшие' ℹ️ не всегда могут справиться "
                                               " без нашей помощи. Они нуждаются в защите и заботе, "
                                               " и каждый из нас может сделать свой вклад. 🆘"
                                               " Если вы чувствуете, что готовы подарить часть своего времени и любви "
                                               " этим удивительным созданиям, рассмотрите возможность взять под опеку "
                                               " 'ваше животное'. Ваша поддержка может сделать мир лучше для них."
                                               " Спасибо, что приняли участие в нашей викторине "
                                               " и проявили интерес к животному миру. Вместе мы можем сделать больше! ",
                                               reply_markup=markup)


    elif message.text == 'Попробовать еще раз':
        try_again(message)


    elif message.text == 'Оставить отзыв':
        bot.send_message(message.from_user.id, "Пожалуйста, напишите свой отзыв:")
        bot.register_next_step_handler(message, gather_feedback)


    elif message.text == 'Гулять 👣':
        user_id = message.from_user.id
        markup = types.InlineKeyboardMarkup()
        quiz_result = ("Поздравляю! Ваш результат - Южноафриканский пингвин! 🌟 "
                       " Это символ вашей индивидуальности и уникальности. "
                       " Южноафриканский пингвин известен своей способностью выделяться из толпы, "
                       " и вы точно также привлекаете внимание своей харизмой и уникальностью. "
                       " Поздравляем с этим великолепным сравнением! !!!")
        employee_id = id  # Здесь  ID Telegram сотрудника зоопарка
        send_telegram_message(employee_id, f"Пользователь {user_id} успешно прошел викторину")
        image_path = 'F:\Бот\Moscow3оо\images\pingvin.jpg'
        send_post(bot, message, image_path, quiz_result)
        facebook_share_link, vk_share_link = generate_share_links()
        btn1 = types.InlineKeyboardButton(text="Южноафриканский пингвин 🐧",
                                          url='https://moscowzoo.ru/animals/pingvinoobraznye/yuzhnoafrikanskiy-ili-ochkovyy-pingvin/?sphrase_id=737596')
        btn2 = types.InlineKeyboardButton(text="Взять под опеку ❕", url='https://moscowzoo.ru/my-zoo/become-a-guardian/')
        btn_facebook = types.InlineKeyboardButton(" 🔲Поделиться в Facebook🔲", url=facebook_share_link)
        btn_vk = types.InlineKeyboardButton("🔲Поделиться в VK🔲", url=vk_share_link)
        markup.add(btn_facebook, btn1, btn2, btn_vk)
        bot.send_message(message.from_user.id, "Нажмите на кнопку 🔲, чтобы поделиться своим результатом или "
                                               " узнать больше о выбранном вами животном. "
                                               " Ведь каждое из них уникально и заслуживает нашего внимания."
                                               " Но помните, наши 'Братья меньшие' ℹ️ не всегда могут справиться "
                                               " без нашей помощи. Они нуждаются в защите и заботе, "
                                               " и каждый из нас может сделать свой вклад. 🆘"
                                               " Если вы чувствуете, что готовы подарить часть своего времени и любви "
                                               " этим удивительным созданиям, рассмотрите возможность взять под опеку "
                                               " 'ваше животное'. Ваша поддержка может сделать мир лучше для них."
                                               " Спасибо, что приняли участие в нашей викторине "
                                               " и проявили интерес к животному миру. Вместе мы можем сделать больше! ",
                                               reply_markup=markup)


    elif message.text == 'Попробовать еще раз':
        try_again(message)


    elif message.text == 'Оставить отзыв':
        bot.send_message(message.from_user.id, "Пожалуйста, напишите свой отзыв:")
        bot.register_next_step_handler(message, gather_feedback)


    elif message.text == 'Ночь 🌑':
        user_id = message.from_user.id
        markup = types.InlineKeyboardMarkup()
        quiz_result = ("Поздравляю! Ваша обаятельная нежность и мягкость делают "
                       " вас похожим на милую и приятную сову-сплюшку. "
                       " Вы обладаете спокойной мудростью и радостным настроением, "
                       " которые приносят тепло и уют окружающим. "
                       " Ваша доброта и забота делают мир ярче и добрее!!!")
        employee_id = id  # Здесь  ID Telegram сотрудника зоопарка
        send_telegram_message(employee_id, f"Пользователь {user_id} успешно прошел викторину")
        image_path = 'F:\Бот\Moscow3оо\images\splushka.jpg'
        send_post(bot, message, image_path, quiz_result)
        facebook_share_link, vk_share_link = generate_share_links()
        btn1 = types.InlineKeyboardButton(text='СПЛЮШКА 🦉',
                                          url='https://moscowzoo.ru/animals/sovoobraznye/splyushka/?sphrase_id=741226')
        btn2 = types.InlineKeyboardButton(text="Взять под опеку ❕", url='https://moscowzoo.ru/my-zoo/become-a-guardian/')
        btn_facebook = types.InlineKeyboardButton(" 🔲Поделиться в Facebook🔲", url=facebook_share_link)
        btn_vk = types.InlineKeyboardButton("🔲Поделиться в VK🔲", url=vk_share_link)
        markup.add(btn_facebook, btn1, btn2, btn_vk)
        bot.send_message(message.from_user.id, "Нажмите на кнопку 🔲, чтобы поделиться своим результатом или "
                                               " узнать больше о выбранном вами животном. "
                                               " Ведь каждое из них уникально и заслуживает нашего внимания."
                                               " Но помните, наши 'Братья меньшие' ℹ️ не всегда могут справиться "
                                               " без нашей помощи. Они нуждаются в защите и заботе, "
                                               " и каждый из нас может сделать свой вклад. 🆘"
                                               " Если вы чувствуете, что готовы подарить часть своего времени и любви "
                                               " этим удивительным созданиям, рассмотрите возможность взять под опеку "
                                               " 'ваше животное'. Ваша поддержка может сделать мир лучше для них."
                                               " Спасибо, что приняли участие в нашей викторине "
                                               " и проявили интерес к животному миру. Вместе мы можем сделать больше! ",
                                               reply_markup=markup)


    elif message.text == 'Попробовать еще раз':
        try_again(message)


    elif message.text == 'Оставить отзыв':
        bot.send_message(message.from_user.id, "Пожалуйста, напишите свой отзыв:")
        bot.register_next_step_handler(message, gather_feedback)


    elif message.text == 'Летать над рекой 🦩':
        user_id = message.from_user.id
        markup = types.InlineKeyboardMarkup()
        quiz_result = ("Поздравляю вас с таким интересным результатом! 🦩"
                       " Алый или красный ибис - это изящная и красивая птица, "
                       " символизирующая грацию, изысканность и утонченность. "
                       " Вас, должно быть, отличают элегантность и привлекательная харизма, "
                       " вы умеете привлекать внимание своим шармом и утонченным вкусом. "
                       " Ваше участие делает окружающую среду более яркой и привлекательной, "
                       " как и красота красного ибиса в природе. !!!")
        employee_id = id  # Здесь  ID Telegram сотрудника зоопарка
        send_telegram_message(employee_id, f"Пользователь {user_id} успешно прошел викторину")
        image_path = 'F:\Бот\Moscow3оо\images\ibis.jpg'
        send_post(bot, message, image_path, quiz_result)
        facebook_share_link, vk_share_link = generate_share_links()
        btn1 = types.InlineKeyboardButton(text='АЛЫЙ ИЛИ КРАСНЫЙ ИБИС 🦩',
                                          url='https://moscowzoo.ru/animals/aistoobraznye/alyy-ili-krasnyy-ibis/?sphrase_id=737597')
        btn2 = types.InlineKeyboardButton(text="Взять под опеку ❕", url='https://moscowzoo.ru/my-zoo/become-a-guardian/')
        btn_facebook = types.InlineKeyboardButton(" 🔲Поделиться в Facebook🔲", url=facebook_share_link)
        btn_vk = types.InlineKeyboardButton("🔲Поделиться в VK🔲", url=vk_share_link)
        markup.add(btn_facebook, btn1, btn2, btn_vk)
        bot.send_message(message.from_user.id, "Нажмите на кнопку 🔲, чтобы поделиться своим результатом или "
                                               " узнать больше о выбранном вами животном. "
                                               " Ведь каждое из них уникально и заслуживает нашего внимания."
                                               " Но помните, наши 'Братья меньшие' ℹ️ не всегда могут справиться "
                                               " без нашей помощи. Они нуждаются в защите и заботе, "
                                               " и каждый из нас может сделать свой вклад. 🆘"
                                               " Если вы чувствуете, что готовы подарить часть своего времени и любви "
                                               " этим удивительным созданиям, рассмотрите возможность взять под опеку "
                                               " 'ваше животное'. Ваша поддержка может сделать мир лучше для них."
                                               " Спасибо, что приняли участие в нашей викторине "
                                               " и проявили интерес к животному миру. Вместе мы можем сделать больше! ",
                                               reply_markup=markup)


    elif message.text == 'Попробовать еще раз':
        try_again(message)


    elif message.text == 'Оставить отзыв':
        bot.send_message(message.from_user.id, "Пожалуйста, напишите свой отзыв:")
        bot.register_next_step_handler(message, gather_feedback)


    elif message.text == 'Лето 🌞':
        user_id = message.from_user.id
        markup = types.InlineKeyboardMarkup()
        quiz_result = ("Поздравляю! Вам очень идет черный аист! 🐦‍⬛ "
                       " Это величественная и изящная птица, символизирующая глубокие эмоции, "
                       " таинственность и утонченность. "
                       " Вам, должно быть, присуща загадочность и притягательная индивидуальность, "
                       " и вы умеете привлекать внимание своей аурой таинственности. "
                       " Ваша элегантность и интригующий характер делают вас привлекательным, подобно черному аисту, "
                       " пленяющему своим очарованием!!!")
        employee_id = id  # Здесь  ID Telegram сотрудника зоопарка
        send_telegram_message(employee_id, f"Пользователь {user_id} успешно прошел викторину")
        image_path = 'F:\Бот\Moscow3оо\images\Aist.jpg'
        send_post(bot, message, image_path, quiz_result)
        facebook_share_link, vk_share_link = generate_share_links()
        btn1 = types.InlineKeyboardButton(text='ЧЕРНЫЙ АИСТ 🐦‍⬛',
                                          url='https://moscowzoo.ru/animals/aistoobraznye/chernyy-aist/?sphrase_id=741223')
        btn2 = types.InlineKeyboardButton(text="Взять под опеку ❕", url='https://moscowzoo.ru/my-zoo/become-a-guardian/')
        btn_facebook = types.InlineKeyboardButton(" 🔲Поделиться в Facebook🔲", url=facebook_share_link)
        btn_vk = types.InlineKeyboardButton("🔲Поделиться в VK🔲", url=vk_share_link)
        markup.add(btn_facebook, btn1, btn2, btn_vk)
        bot.send_message(message.from_user.id, "Нажмите на кнопку 🔲, чтобы поделиться своим результатом или "
                                               " узнать больше о выбранном вами животном. "
                                               " Ведь каждое из них уникально и заслуживает нашего внимания."
                                               " Но помните, наши 'Братья меньшие' ℹ️ не всегда могут справиться "
                                               " без нашей помощи. Они нуждаются в защите и заботе, "
                                               " и каждый из нас может сделать свой вклад. 🆘"
                                               " Если вы чувствуете, что готовы подарить часть своего времени и любви "
                                               " этим удивительным созданиям, рассмотрите возможность взять под опеку "
                                               " 'ваше животное'. Ваша поддержка может сделать мир лучше для них."
                                               " Спасибо, что приняли участие в нашей викторине "
                                               " и проявили интерес к животному миру. Вместе мы можем сделать больше! ",
                                               reply_markup=markup)

    elif message.text == 'Попробовать еще раз':
        try_again(message)


    elif message.text == 'Оставить отзыв':
        bot.send_message(message.from_user.id, "Пожалуйста, напишите свой отзыв:")
        bot.register_next_step_handler(message, gather_feedback)


    elif message.text == 'Вода 💧':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mar = types.KeyboardButton('Хочу себе крылья 🐟')
        mar1 = types.KeyboardButton('Хочу веселья 🐠')
        mar2 = types.KeyboardButton('Хочу погреться 🦎')
        mar3 = types.KeyboardButton('Не хочу спешить 🐢')
        mar4 = types.KeyboardButton('Хочу кусаться 🐊:)')
        mar5 = types.KeyboardButton('Оставить отзыв')
        mar6 = types.KeyboardButton('Назад в меню')
        mar7 = types.KeyboardButton("Попробовать еще раз")
        markup.add(mar, mar1, mar2, mar3, mar4, mar5, mar6, mar7)
        bot.send_message(message.from_user.id, "Превосходно, ведь мы все на 80% состоим из воды, "
                                               " а те, кто чувствует себя ближе к воде, возможно, даже на 85% :). "
                                               " Давайте совершим ещё несколько выборов, чтобы я мог лучше узнать вас.",
                                                reply_markup=markup)


    elif message.text == 'Назад в меню':
        handle_message(message)


    elif message.text == 'Оставить отзыв':
        bot.send_message(message.from_user.id, "Пожалуйста, напишите свой отзыв:")
        bot.register_next_step_handler(message, gather_feedback)


    elif message.text == 'Хочу себе крылья 🐟':
        user_id = message.from_user.id
        markup = types.InlineKeyboardMarkup()
        quiz_result = ("Поздравляю вас! Ваша уникальность и неповторимость напоминают мне о момбасской крылатке, "
                        " великолепной и уникальной рыбе Индийского океана. "
                        " Ваша способность выделяться, ваше смелое и яркое внутреннее"
                        " 'я'  делают вас по-настоящему особенным, как этот великолепный обитатель подводного мира."
                        " Пусть момбасская крылатка будет вашим символом уникальности и смелости, "
                        " и пусть она всегда вдохновляет вас на новые достижения. "
                        " Поздравляю вас с этим уникальным сочетанием качеств и желаю, "
                        " чтобы ваша жизнь была полна смелых и ярких моментов! 🐟 ")

        employee_id = id  # Здесь  ID Telegram сотрудника зоопарка
        send_telegram_message(employee_id, f"Пользователь {user_id} успешно прошел викторину")
        image_path = 'F:\Бот\Moscow3оо\images\m.kp.jpg'
        send_post(bot, message, image_path, quiz_result)
        facebook_share_link, vk_share_link = generate_share_links()
        btn1 = types.InlineKeyboardButton(text='МОМБАССКАЯ КРЫЛАТКА 🐟',
                                          url='https://moscowzoo.ru/animals/skorpenoobraznye/mombasskaya-krylatka/?sphrase_id=737797')
        btn2 = types.InlineKeyboardButton(text="Взять под опеку ❕", url='https://moscowzoo.ru/my-zoo/become-a-guardian/')
        btn_facebook = types.InlineKeyboardButton(" 🔲Поделиться в Facebook🔲", url=facebook_share_link)
        btn_vk = types.InlineKeyboardButton("🔲Поделиться в VK🔲", url=vk_share_link)
        markup.add(btn_facebook, btn1, btn2, btn_vk)
        bot.send_message(message.from_user.id, "Нажмите на кнопку 🔲, чтобы поделиться своим результатом или "
                                               " узнать больше о выбранном вами животном. "
                                               " Ведь каждое из них уникально и заслуживает нашего внимания."
                                               " Но помните, наши 'Братья меньшие' ℹ️ не всегда могут справиться "
                                               " без нашей помощи. Они нуждаются в защите и заботе, "
                                               " и каждый из нас может сделать свой вклад. 🆘"
                                               " Если вы чувствуете, что готовы подарить часть своего времени и любви "
                                               " этим удивительным созданиям, рассмотрите возможность взять под опеку "
                                               " 'ваше животное'. Ваша поддержка может сделать мир лучше для них."
                                               " Спасибо, что приняли участие в нашей викторине "
                                               " и проявили интерес к животному миру. Вместе мы можем сделать больше! ",
                                               reply_markup=markup)

    elif message.text == 'Попробовать еще раз':
        try_again(message)


    elif message.text == 'Оставить отзыв':
        bot.send_message(message.from_user.id, "Пожалуйста, напишите свой отзыв:")
        bot.register_next_step_handler(message, gather_feedback)


    elif message.text == 'Хочу веселья 🐠':
        user_id = message.from_user.id
        markup = types.InlineKeyboardMarkup()
        quiz_result = ("Поздравляю вас! Ваша яркость и способность приспосабливаться к обстоятельствам "
                       " напоминают мне о ложном клоуне, уникальной рыбе теплых морей. "
                       " Ваша энергия, ваше цветное настроение и ваша уникальная личность делают"
                       " вас по-настоящему особенным, как этот яркий обитатель коралловых рифов. "
                       " Пусть ложный клоун будет вашим символом энергии и приспособляемости, "
                       " и пусть он всегда вдохновляет вас на новые достижения. "
                       " Поздравляю вас с этим уникальным сочетанием качеств и желаю, "
                       " чтобы ваша жизнь была полна радости и успехов 🐠! ")

        employee_id = id  # Здесь  ID Telegram сотрудника зоопарка
        send_telegram_message(employee_id, f"Пользователь {user_id} успешно прошел викторину")
        image_path = 'F:\Бот\Moscow3оо\images\cloun.jpg'
        send_post(bot, message, image_path, quiz_result)
        facebook_share_link, vk_share_link = generate_share_links()
        btn1 = types.InlineKeyboardButton(text='ЛОЖНЫЙ КЛОУН 🐠',
                                          url='https://moscowzoo.ru/animals/okuneobraznye/anemonovaya-ryba-lozhnyy-kloun/?sphrase')
        btn2 = types.InlineKeyboardButton(text="Взять под опеку ❕", url='https://moscowzoo.ru/my-zoo/become-a-guardian/')
        btn_facebook = types.InlineKeyboardButton(" 🔲Поделиться в Facebook🔲", url=facebook_share_link)
        btn_vk = types.InlineKeyboardButton("🔲Поделиться в VK🔲", url=vk_share_link)
        markup.add(btn_facebook, btn1, btn2, btn_vk)
        bot.send_message(message.from_user.id, "Нажмите на кнопку 🔲, чтобы поделиться своим результатом или "
                                               " узнать больше о выбранном вами животном. "
                                               " Ведь каждое из них уникально и заслуживает нашего внимания."
                                               " Но помните, наши 'Братья меньшие' ℹ️ не всегда могут справиться "
                                               " без нашей помощи. Они нуждаются в защите и заботе, "
                                               " и каждый из нас может сделать свой вклад. 🆘"
                                               " Если вы чувствуете, что готовы подарить часть своего времени и любви "
                                               " этим удивительным созданиям, рассмотрите возможность взять под опеку "
                                               " 'ваше животное'. Ваша поддержка может сделать мир лучше для них."
                                               " Спасибо, что приняли участие в нашей викторине "
                                               " и проявили интерес к животному миру. Вместе мы можем сделать больше! ",
                                               reply_markup=markup)


    elif message.text == 'Попробовать еще раз':
        try_again(message)


    elif message.text == 'Оставить отзыв':
        bot.send_message(message.from_user.id, "Пожалуйста, напишите свой отзыв:")
        bot.register_next_step_handler(message, gather_feedback)


    elif message.text == 'Хочу погреться 🦎':
        user_id = message.from_user.id
        markup = types.InlineKeyboardMarkup()
        quiz_result = ("Поздравляю вас! Ваша способность адаптироваться к любым обстоятельствам"
                       " и ваше долголетие напоминают мне о зелёной игуане, величественном существе тропических лесов. "
                       " Ваша гибкость, ваша упорность и ваше стремление к долгой и плодотворной жизни делают "
                       " вас по-настоящему уникальным, как этот яркий обитатель тропиков. "
                       " Пусть зелёная игуана будет вашим символом адаптивности и долголетия,  "
                       " и пусть она всегда вдохновляет вас на новые достижения. "
                       " Поздравляю вас с этим уникальным сочетанием качеств и желаю, "
                       " чтобы ваша жизнь была полна успехов и долголетия! 🦎! ")
        employee_id = id  # Здесь  ID Telegram сотрудника зоопарка
        send_telegram_message(employee_id, f"Пользователь {user_id} успешно прошел викторину")
        image_path = 'F:\Бот\Moscow3оо\images\iguana.jpg'
        send_post(bot, message, image_path, quiz_result)
        facebook_share_link, vk_share_link = generate_share_links()
        btn1 = types.InlineKeyboardButton(text='Обыкновенная или зелёная игуана 🦎',
                                          url='https://moscowzoo.ru/animals/cheshuichatye/obyknovennaya-iguana/?sphrase')
        btn2 = types.InlineKeyboardButton(text="Взять под опеку ❕", url='https://moscowzoo.ru/my-zoo/become-a-guardian/')
        btn_facebook = types.InlineKeyboardButton(" 🔲Поделиться в Facebook🔲", url=facebook_share_link)
        btn_vk = types.InlineKeyboardButton("🔲Поделиться в VK🔲", url=vk_share_link)
        markup.add(btn_facebook, btn1, btn2, btn_vk)
        bot.send_message(message.from_user.id, "Нажмите на кнопку 🔲, чтобы поделиться своим результатом или "
                                               " узнать больше о выбранном вами животном. "
                                               " Ведь каждое из них уникально и заслуживает нашего внимания."
                                               " Но помните, наши 'Братья меньшие' ℹ️ не всегда могут справиться "
                                               " без нашей помощи. Они нуждаются в защите и заботе, "
                                               " и каждый из нас может сделать свой вклад. 🆘"
                                               " Если вы чувствуете, что готовы подарить часть своего времени и любви "
                                               " этим удивительным созданиям, рассмотрите возможность взять под опеку "
                                               " 'ваше животное'. Ваша поддержка может сделать мир лучше для них."
                                               " Спасибо, что приняли участие в нашей викторине "
                                               " и проявили интерес к животному миру. Вместе мы можем сделать больше! ",
                                               reply_markup=markup)


    elif message.text == 'Попробовать еще раз':
        try_again(message)


    elif message.text == 'Оставить отзыв':
        bot.send_message(message.from_user.id, "Пожалуйста, напишите свой отзыв:")
        bot.register_next_step_handler(message, gather_feedback)


    elif message.text == 'Не хочу спешить 🐢':
        user_id = message.from_user.id
        markup = types.InlineKeyboardMarkup()
        quiz_result = ("Поздравляю вас! Вам идеально подходит  СЛОНОВАЯ ЧЕРЕПАХА 🐢 - "
                       " существо, объединяющего мудрость и стойкость. "
                       " Вы обладаете не только силой и устойчивостью слона, но и мудростью и долголетием черепахи. "
                       " Ваше присутствие наполняет пространство гармонией и умиротворением, "
                       " а ваша настойчивость и терпение помогают вам преодолевать любые преграды на пути к успеху. "
                       " Позвольте СЛОНОВОЙ ЧЕРЕПАХЕ 🐢 стать вашим символом силы, мудрости и долголетия, "
                       " и пусть она всегда будет вдохновлять вас на достижение великих высот. "
                       " Поздравляю вас с этим уникальным сочетанием качеств и желаю, "
                       " чтобы ваша жизнь была наполнена радостью, успехами и миром! !!!")
        employee_id = id # Здесь  ID Telegram сотрудника зоопарка
        send_telegram_message(employee_id, f"Пользователь {user_id} успешно прошел викторину")
        image_path = 'F:\Бот\Moscow3оо\images\iertle.jpg'
        send_post(bot, message, image_path, quiz_result)
        facebook_share_link, vk_share_link = generate_share_links()
        btn1 = types.InlineKeyboardButton(text='СЛОНОВАЯ ЧЕРЕПАХА 🐢',
                                          url='https://moscowzoo.ru/animals/cherepakhi/slonovaya-cherepakha/?sphrase_id=737800')
        btn2 = types.InlineKeyboardButton(text="Взять под опеку ❕", url='https://moscowzoo.ru/my-zoo/become-a-guardian/')
        btn_facebook = types.InlineKeyboardButton(" 🔲Поделиться в Facebook🔲", url=facebook_share_link)
        btn_vk = types.InlineKeyboardButton("🔲Поделиться в VK🔲", url=vk_share_link)
        markup.add(btn_facebook, btn1, btn2, btn_vk)
        bot.send_message(message.from_user.id, "Нажмите на кнопку 🔲, чтобы поделиться своим результатом или "
                                               " узнать больше о выбранном вами животном. "
                                               " Ведь каждое из них уникально и заслуживает нашего внимания."
                                               " Но помните, наши 'Братья меньшие' ℹ️ не всегда могут справиться "
                                               " без нашей помощи. Они нуждаются в защите и заботе, "
                                               " и каждый из нас может сделать свой вклад. 🆘"
                                               " Если вы чувствуете, что готовы подарить часть своего времени и любви "
                                               " этим удивительным созданиям, рассмотрите возможность взять под опеку "
                                               " 'ваше животное'. Ваша поддержка может сделать мир лучше для них."
                                               " Спасибо, что приняли участие в нашей викторине "
                                               " и проявили интерес к животному миру. Вместе мы можем сделать больше! ",
                                               reply_markup=markup)


    elif message.text == 'Попробовать еще раз':
        try_again(message)


    elif message.text == 'Оставить отзыв':
        bot.send_message(message.from_user.id, "Пожалуйста, напишите свой отзыв:")
        bot.register_next_step_handler(message, gather_feedback)


    elif message.text == 'Хочу кусаться 🐊:)':
        user_id = message.from_user.id
        markup = types.InlineKeyboardMarkup()
        quiz_result = ("Поздравляю вас! Вам идеально подходит ГАВИАЛОВЫЙ КРОКОДИЛ 🐊 - "
                       " могучий и величественный существо, которое воплощает силу и изящество. "
                       " Вы обладаете не только мощными способностями адаптации и выживания, характерными для крокодила,"
                       " но и уникальной элегантностью и изяществом гавиала. "
                       " Ваша присутствие наполняет пространство магией и внушает уважение, "
                       " а ваша сила и решительность помогают вам преодолевать любые преграды на пути к успеху. "
                       " Позвольте ГАВИАЛОВОМУ КРОКОДИЛУ 🐊 стать вашим символом силы, грации и уверенности, "
                       " и пусть он всегда будет вдохновлять вас на достижение великих вершин. "
                       " Поздравляю вас с этим уникальным сочетанием качеств и желаю, "
                       " чтобы ваша жизнь была наполнена приключениями, успехами и благополучием!")
        employee_id = id  # Здесь  ID Telegram сотрудника зоопарка
        send_telegram_message(employee_id, f"Пользователь {user_id} успешно прошел викторину")
        image_path = 'F:\Бот\Moscow3оо\images\croco.jpg'
        send_post(bot, message, image_path, quiz_result)
        facebook_share_link, vk_share_link = generate_share_links()
        btn1 = types.InlineKeyboardButton(text='ГАВИАЛОВЫЙ КРОКОДИЛ 🐊',
                                          url='https://moscowzoo.ru/animals/krokodily/gavialovyy-krokodil/?sphrase_id=737802')
        btn2 = types.InlineKeyboardButton(text="Взять под опеку ❕", url='https://moscowzoo.ru/my-zoo/become-a-guardian/')
        btn_facebook = types.InlineKeyboardButton(" 🔲Поделиться в Facebook🔲", url=facebook_share_link)
        btn_vk = types.InlineKeyboardButton("🔲Поделиться в VK🔲", url=vk_share_link)
        markup.add(btn_facebook, btn1, btn2, btn_vk)
        bot.send_message(message.from_user.id, "Нажмите на кнопку 🔲, чтобы поделиться своим результатом или "
                                               " узнать больше о выбранном вами животном. "
                                               " Ведь каждое из них уникально и заслуживает нашего внимания."
                                               " Но помните, наши 'Братья меньшие' ℹ️ не всегда могут справиться "
                                               " без нашей помощи. Они нуждаются в защите и заботе, "
                                               " и каждый из нас может сделать свой вклад. 🆘"
                                               " Если вы чувствуете, что готовы подарить часть своего времени и любви "
                                               " этим удивительным созданиям, рассмотрите возможность взять под опеку "
                                               " 'ваше животное'. Ваша поддержка может сделать мир лучше для них."
                                               " Спасибо, что приняли участие в нашей викторине "
                                               " и проявили интерес к животному миру. Вместе мы можем сделать больше! ",
                                               reply_markup=markup)



    elif message.text == 'Попробовать еще раз':
        try_again(message)


    elif message.text == 'Оставить отзыв':
        bot.send_message(message.from_user.id, "Пожалуйста, напишите свой отзыв:")
        bot.register_next_step_handler(message, gather_feedback)


    elif message.text == 'Земля 🌎':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mar = types.KeyboardButton('Кота 🐈')
        mar1 = types.KeyboardButton('Обезьянку 🐵')
        mar2 = types.KeyboardButton('Куницу 🦝')
        mar3 = types.KeyboardButton('Лошадь 🐴')
        mar4 = types.KeyboardButton('Броненосца 🦖')
        mar5 = types.KeyboardButton('Оставить отзыв')
        mar6 = types.KeyboardButton('Назад в меню')
        mar7 = types.KeyboardButton("Попробовать еще раз")
        markup.add(mar, mar1, mar2, mar3, mar4, mar5, mar6, mar7)
        bot.send_message(message.from_user.id, "Здравствуйте, тут я вам предложу произвести выбор кого-бы вы взяли себе"
                                               " как домашнее животное, не все варианты конечно очевидные как казало бы"
                                               " в каждом из вариантов вы найдете что-то новое для себя, возможно"
                                               " произойдет любовь с 'первого взгляда'", reply_markup=markup)


    elif message.text == 'Кота 🐈':
        user_id = message.from_user.id
        markup = types.InlineKeyboardMarkup()
        quiz_result = ("Поздравляю вас! Вам идеально подходит  Камышовый кот 🐈 - загадочный и изящный создание, "
                       " которое воплощает грацию и независимость. "
                       " Вы обладаете не только таинственностью и ловкостью кота, "
                       " но и способностью приспособиться к любой ситуации, как камышовый кот в водной среде. "
                       " Ваше присутствие наполняет пространство теплотой и умиротворением, "
                       " а ваша независимость и интуиция помогают вам найти свой путь в жизни. "
                       " Позвольте Камышовому коту 🐈 стать вашим символом грации, независимости и интуиции, "
                       " и пусть он всегда будет вдохновлять вас на открытие новых горизонтов. "
                       " Поздравляю вас с этим уникальным сочетанием качеств и желаю, "
                       " чтобы ваша жизнь была наполнена приключениями, радостью и самовыражением!")
        employee_id = id  # Здесь  ID Telegram сотрудника зоопарка
        send_telegram_message(employee_id, f"Пользователь {user_id} успешно прошел викторину")
        image_path = 'F:\Бот\Moscow3оо\images\cat.jpg'
        send_post(bot, message, image_path, quiz_result)
        facebook_share_link, vk_share_link = generate_share_links()
        btn1 = types.InlineKeyboardButton(text='Камышовый кот 🐈',
                                          url='https://moscowzoo.ru/animals/khishchnye/kamyshovyy-kot/?sphrase_id=738172')
        btn2 = types.InlineKeyboardButton(text="Взять под опеку ❕", url='https://moscowzoo.ru/my-zoo/become-a-guardian/')
        btn_facebook = types.InlineKeyboardButton(" 🔲Поделиться в Facebook🔲", url=facebook_share_link)
        btn_vk = types.InlineKeyboardButton("🔲Поделиться в VK🔲", url=vk_share_link)
        markup.add(btn_facebook, btn1, btn2, btn_vk)
        bot.send_message(message.from_user.id, "Нажмите на кнопку 🔲, чтобы поделиться своим результатом или "
                                               " узнать больше о выбранном вами животном. "
                                               " Ведь каждое из них уникально и заслуживает нашего внимания."
                                               " Но помните, наши 'Братья меньшие' ℹ️ не всегда могут справиться "
                                               " без нашей помощи. Они нуждаются в защите и заботе, "
                                               " и каждый из нас может сделать свой вклад. 🆘"
                                               " Если вы чувствуете, что готовы подарить часть своего времени и любви "
                                               " этим удивительным созданиям, рассмотрите возможность взять под опеку "
                                               " 'ваше животное'. Ваша поддержка может сделать мир лучше для них."
                                               " Спасибо, что приняли участие в нашей викторине "
                                               " и проявили интерес к животному миру. Вместе мы можем сделать больше! ",
                                               reply_markup=markup)


    elif message.text == 'Попробовать еще раз':
        try_again(message)


    elif message.text == 'Оставить отзыв':
        bot.send_message(message.from_user.id, "Пожалуйста, напишите свой отзыв:")
        bot.register_next_step_handler(message, gather_feedback)


    elif message.text == 'Обезьянку 🐵':
        user_id = message.from_user.id
        markup = types.InlineKeyboardMarkup()
        quiz_result = ("🐵Поздравляю вас! Ваше внутреннее сияние и способность работать в "
                       " команде напоминают мне о Золотистом тамарине, уникальном создании тропических лесов."
                       " Ваша способность взаимодействовать с другими, "
                       " ваша социальность и ваша уникальная личность делают вас по-настоящему особенным, "
                       " как этот яркий обитатель джунглей. "
                       " Пусть Золотистый тамарин будет вашим символом командной работы и уникальности, "
                       " и пусть он всегда вдохновляет вас на новые свершения. "
                       " Поздравляю вас с этим уникальным сочетанием качеств и желаю, "
                       " чтобы ваша жизнь была полна сияния и успехов!")
        employee_id = id  # Здесь  ID Telegram сотрудника зоопарка
        send_telegram_message(employee_id, f"Пользователь {user_id} успешно прошел викторину")
        image_path = 'F:\Бот\Moscow3оо\images\marin.jpg'
        send_post(bot, message, image_path, quiz_result)
        facebook_share_link, vk_share_link = generate_share_links()
        btn1 = types.InlineKeyboardButton(text='ЗОЛОТИСТЫЙ ТАМАРИН 🐵',
                                          url='https://moscowzoo.ru/animals/primaty/zolotistyy-tamarin/?sphrase')
        btn2 = types.InlineKeyboardButton(text="Взять под опеку ❕", url='https://moscowzoo.ru/my-zoo/become-a-guardian/')
        btn_facebook = types.InlineKeyboardButton(" 🔲Поделиться в Facebook🔲", url=facebook_share_link)
        btn_vk = types.InlineKeyboardButton("🔲Поделиться в VK🔲", url=vk_share_link)
        markup.add(btn_facebook, btn1, btn2, btn_vk)
        bot.send_message(message.from_user.id, "Нажмите на кнопку 🔲, чтобы поделиться своим результатом или "
                                               " узнать больше о выбранном вами животном. "
                                               " Ведь каждое из них уникально и заслуживает нашего внимания."
                                               " Но помните, наши 'Братья меньшие' ℹ️ не всегда могут справиться "
                                               " без нашей помощи. Они нуждаются в защите и заботе, "
                                               " и каждый из нас может сделать свой вклад. 🆘"
                                               " Если вы чувствуете, что готовы подарить часть своего времени и любви "
                                               " этим удивительным созданиям, рассмотрите возможность взять под опеку "
                                               " 'ваше животное'. Ваша поддержка может сделать мир лучше для них."
                                               " Спасибо, что приняли участие в нашей викторине "
                                               " и проявили интерес к животному миру. Вместе мы можем сделать больше! ",
                                               reply_markup=markup)


    elif message.text == 'Попробовать еще раз':
        try_again(message)


    elif message.text == 'Оставить отзыв':
        bot.send_message(message.from_user.id, "Пожалуйста, напишите свой отзыв:")
        bot.register_next_step_handler(message, gather_feedback)



    elif message.text == 'Куницу 🦝':
        user_id = message.from_user.id
        markup = types.InlineKeyboardMarkup()
        quiz_result = ("Поздравляю вас! Вы идеально подходите для воплощения Харзы 🦝 - умного и хитрого существа, "
                       " которое воплощает смекалку и изобретательность. "
                       " Вы обладаете не только острым умом и наблюдательностью, характерными для харзы, "
                       " но и способностью находить нестандартные решения и преодолевать преграды. "
                       " Ваше присутствие наполняет пространство весельем и энергией, "
                       " а ваша хитрость и находчивость помогают вам достигать поставленных целей. "
                       " Позвольте Харзе 🦝 стать вашим символом умения приспосабливаться и "
                       " находить выходы из любых ситуаций, и пусть она всегда будет вдохновлять вас "
                       " на творческие подходы и новые возможности. "
                       " Поздравляю вас с этим уникальным сочетанием качеств и желаю, "
                       " чтобы ваша жизнь была наполнена приключениями, успехами и радостью!")
        employee_id = id  # Здесь  ID Telegram сотрудника зоопарка
        send_telegram_message(employee_id, f"Пользователь {user_id} успешно прошел викторину")
        image_path = 'F:\Бот\Moscow3оо\images\harza.jpg'
        send_post(bot, message, image_path, quiz_result)
        facebook_share_link, vk_share_link = generate_share_links()
        btn1 = types.InlineKeyboardButton(text='ХАРЗА 🦝',
                                          url='https://moscowzoo.ru/animals/khishchnye/kharza/?sphrase')
        btn2 = types.InlineKeyboardButton(text="Взять под опеку ❕", url='https://moscowzoo.ru/my-zoo/become-a-guardian/')
        btn_facebook = types.InlineKeyboardButton(" 🔲Поделиться в Facebook🔲", url=facebook_share_link)
        btn_vk = types.InlineKeyboardButton("🔲Поделиться в VK🔲", url=vk_share_link)
        markup.add(btn_facebook, btn1, btn2, btn_vk)
        bot.send_message(message.from_user.id, "Нажмите на кнопку 🔲, чтобы поделиться своим результатом или "
                                               " узнать больше о выбранном вами животном. "
                                               " Ведь каждое из них уникально и заслуживает нашего внимания."
                                               " Но помните, наши 'Братья меньшие' ℹ️ не всегда могут справиться "
                                               " без нашей помощи. Они нуждаются в защите и заботе, "
                                               " и каждый из нас может сделать свой вклад. 🆘"
                                               " Если вы чувствуете, что готовы подарить часть своего времени и любви "
                                               " этим удивительным созданиям, рассмотрите возможность взять под опеку "
                                               " 'ваше животное'. Ваша поддержка может сделать мир лучше для них."
                                               " Спасибо, что приняли участие в нашей викторине "
                                               " и проявили интерес к животному миру. Вместе мы можем сделать больше! ",
                                               reply_markup=markup)


    elif message.text == 'Попробовать еще раз':
        try_again(message)


    elif message.text == 'Оставить отзыв':
        bot.send_message(message.from_user.id, "Пожалуйста, напишите свой отзыв:")
        bot.register_next_step_handler(message, gather_feedback)


    elif message.text == 'Лошадь 🐴':
        user_id = message.from_user.id
        markup = types.InlineKeyboardMarkup()
        quiz_result = ("Поздравляю вас! Вы идеально подходит Лошадь Пржевальского 🐴 - сильного и выносливого существа, "
                       " которое символизирует свободу и дикую красоту. "
                       " Вы обладаете не только грацией и элегантностью, характерными для лошади, "
                       " но и силой духа и упорством. Ваша энергия и стойкость позволяют вам преодолевать любые преграды "
                       " и добиваться поставленных целей. Ваше присутствие наполняет пространство свежим ветром свободы, "
                       " а ваша готовность к приключениям вдохновляет окружающих. "
                       " Позвольте Лошади Пржевальского 🐴 стать вашим символом стойкости и решительности, "
                       " и пусть она всегда будет вести вас по пути успеха и свободы. "
                       " Поздравляю вас с этим уникальным сочетанием качеств и желаю, "
                       " чтобы ваша жизнь была наполнена приключениями, радостью и свободой!")
        employee_id = id  # Здесь  ID Telegram сотрудника зоопарка
        send_telegram_message(employee_id, f"Пользователь {user_id} успешно прошел викторину")
        image_path = 'F:\Бот\Moscow3оо\images\igogo.jpg'
        send_post(bot, message, image_path, quiz_result)
        facebook_share_link, vk_share_link = generate_share_links()
        btn1 = types.InlineKeyboardButton(text='ЛОШАДЬ ПРЖЕВАЛЬСКОГО 🐴',
                                          url='https://moscowzoo.ru/animals/neparnokopytnye/loshad-przhevalskogo/?sphrase')
        btn2 = types.InlineKeyboardButton(text="Взять под опеку ❕", url='https://moscowzoo.ru/my-zoo/become-a-guardian/')
        btn_facebook = types.InlineKeyboardButton(" 🔲Поделиться в Facebook🔲", url=facebook_share_link)
        btn_vk = types.InlineKeyboardButton("🔲Поделиться в VK🔲", url=vk_share_link)
        markup.add(btn_facebook, btn1, btn2, btn_vk)
        bot.send_message(message.from_user.id, "Нажмите на кнопку 🔲, чтобы поделиться своим результатом или "
                                               " узнать больше о выбранном вами животном. "
                                               " Ведь каждое из них уникально и заслуживает нашего внимания."
                                               " Но помните, наши 'Братья меньшие' ℹ️ не всегда могут справиться "
                                               " без нашей помощи. Они нуждаются в защите и заботе, "
                                               " и каждый из нас может сделать свой вклад. 🆘"
                                               " Если вы чувствуете, что готовы подарить часть своего времени и любви "
                                               " этим удивительным созданиям, рассмотрите возможность взять под опеку "
                                               " 'ваше животное'. Ваша поддержка может сделать мир лучше для них."
                                               " Спасибо, что приняли участие в нашей викторине "
                                               " и проявили интерес к животному миру. Вместе мы можем сделать больше! ",
                                               reply_markup=markup)


    elif message.text == 'Попробовать еще раз':
        try_again(message)


    elif message.text == 'Оставить отзыв':
        bot.send_message(message.from_user.id, "Пожалуйста, напишите свой отзыв:")
        bot.register_next_step_handler(message, gather_feedback)


    elif message.text == 'Броненосца 🦖':
        user_id = message.from_user.id
        markup = types.InlineKeyboardMarkup()
        quiz_result = ("Поздравляю вас! Вам идеально подходит воплощения Броненосца🦖 - величественное и мощное существо, "
                       " которое символизирует силу и устойчивость. "
                       " Вы обладаете не только внушительной физической силой и величием, "
                       " характерными для броненосца, но и стойкостью духа и решительностью. "
                       " Ваша сила и уверенность в себе позволяют вам преодолевать любые трудности и преграды. "
                       " Ваше присутствие наполняет пространство силой и авторитетом, "
                       " а ваша устойчивость и непоколебимость вдохновляют окружающих. "
                       " Позвольте Броненосцу 🦖 стать вашим символом мощи и уверенности, "
                       " и пусть он всегда будет защищать вас и помогать вам достигать поставленных целей. "
                       " Поздравляю вас с этим уникальным сочетанием качеств и желаю, "
                       " чтобы ваша жизнь была наполнена силой, достижениями и уверенностью!!!")
        employee_id = id  # Здесь  ID Telegram сотрудника зоопарка
        send_telegram_message(employee_id, f"Пользователь {user_id} успешно прошел викторину")
        image_path = 'F:\Бот\Moscow3оо\images\on.jpg'
        send_post(bot, message, image_path, quiz_result)
        facebook_share_link, vk_share_link = generate_share_links()
        btn1 = types.InlineKeyboardButton(text='Броненосец 🦖',
                                          url='https://moscowzoo.ru/animals/nepolnozubye/sharovidnyy-bronenosets/?sphrase')
        btn2 = types.InlineKeyboardButton(text="Взять под опеку ❕", url='https://moscowzoo.ru/my-zoo/become-a-guardian/')
        btn_facebook = types.InlineKeyboardButton(" 🔲Поделиться в Facebook🔲", url=facebook_share_link)
        btn_vk = types.InlineKeyboardButton("🔲Поделиться в VK🔲", url=vk_share_link)
        markup.add(btn_facebook, btn1, btn2, btn_vk)
        bot.send_message(message.from_user.id, "Нажмите на кнопку 🔲, чтобы поделиться своим результатом или "
                                               " узнать больше о выбранном вами животном. "
                                               " Ведь каждое из них уникально и заслуживает нашего внимания."
                                               " Но помните, наши 'Братья меньшие' ℹ️ не всегда могут справиться "
                                               " без нашей помощи. Они нуждаются в защите и заботе, "
                                               " и каждый из нас может сделать свой вклад. 🆘"
                                               " Если вы чувствуете, что готовы подарить часть своего времени и любви "
                                               " этим удивительным созданиям, рассмотрите возможность взять под опеку "
                                               " 'ваше животное'. Ваша поддержка может сделать мир лучше для них."
                                               " Спасибо, что приняли участие в нашей викторине "
                                               " и проявили интерес к животному миру. Вместе мы можем сделать больше! ",
                                               reply_markup=markup)


    elif message.text == 'Попробовать еще раз':
        try_again(message)


    elif message.text == 'Назад в меню':
        handle_message(message)


    elif message.text == 'Огонь 🔥':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mar = types.KeyboardButton('Овен ♈')
        mar1 = types.KeyboardButton('Овен необыкновенный ♈')
        mar2 = types.KeyboardButton('Стрелец ♐')
        mar3 = types.KeyboardButton('Стрелец v2.0 ♐')
        mar4 = types.KeyboardButton('Лев ♌')
        mar5 = types.KeyboardButton('Оставить отзыв')
        mar6 = types.KeyboardButton('Назад в меню')
        mar7 = types.KeyboardButton("Попробовать еще раз")
        markup.add(mar, mar1, mar2, mar3, mar4, mar5, mar6, mar7)
        bot.send_message(message.from_user.id,"Было увлекательным заданием подбирать для вас животное, "
                                              " соответствующее стихии 'огня', и я рад, что справился с этой задачей. "
                                              " Я надеюсь, что мой выбор принесет вам радость и "
                                              " оставит у вас улыбку на лице. "
                                              " Давайте продолжим: пожалуйста, выберите ваш знак зодиака. "
                                              " Если вашего знака нет в списке, выберите любой, который вам нравится",
                                                reply_markup=markup)


    elif message.text == 'Оставить отзыв':
        bot.send_message(message.from_user.id, "Пожалуйста, напишите свой отзыв:")
        bot.register_next_step_handler(message, gather_feedback)


    elif message.text == 'Овен ♈':
        user_id = message.from_user.id
        markup = types.InlineKeyboardMarkup()
        quiz_result = ("Поздравляю вас! Ваша устойчивость и сила напоминают мне о Дагестанском туре, "
                       " могучем обитателе высоких гор. Ваша способность преодолевать трудности, "
                       " ваша решительность и непоколебимость в достижении целей "
                       " - все это делает вас по-настоящему великим, как этот горный король. "
                       " Пусть Дагестанский тур будет вашим символом силы и упорства,"
                       " и пусть он всегда вдохновляет вас на новые вершины. "
                       " Поздравляю вас с этим уникальным сочетанием качеств и желаю, "
                       " чтобы ваша жизнь была полна достижений и успехов! ♈!!!")
        employee_id = id  # Здесь  ID Telegram сотрудника зоопарка
        send_telegram_message(employee_id, f"Пользователь {user_id} успешно прошел викторину")
        image_path = 'F:\Бот\Moscow3оо\images\dag.jpg'
        send_post(bot, message, image_path, quiz_result)
        facebook_share_link, vk_share_link = generate_share_links()
        btn1 = types.InlineKeyboardButton(text='ДАГЕСТАНСКИЙ ТУР ♈',
                                          url='https://moscowzoo.ru/animals/parnokopytnye/dagestanskiy-vostochnokavkazskiy-tur/?sphrase')
        btn2 = types.InlineKeyboardButton(text="Взять под опеку ❕", url='https://moscowzoo.ru/my-zoo/become-a-guardian/')
        btn_facebook = types.InlineKeyboardButton(" 🔲Поделиться в Facebook🔲", url=facebook_share_link)
        btn_vk = types.InlineKeyboardButton("🔲Поделиться в VK🔲", url=vk_share_link)
        markup.add(btn_facebook, btn1, btn2, btn_vk)
        bot.send_message(message.from_user.id, "Нажмите на кнопку 🔲, чтобы поделиться своим результатом или "
                                               " узнать больше о выбранном вами животном. "
                                               " Ведь каждое из них уникально и заслуживает нашего внимания."
                                               " Но помните, наши 'Братья меньшие' ℹ️ не всегда могут справиться "
                                               " без нашей помощи. Они нуждаются в защите и заботе, "
                                               " и каждый из нас может сделать свой вклад. 🆘"
                                               " Если вы чувствуете, что готовы подарить часть своего времени и любви "
                                               " этим удивительным созданиям, рассмотрите возможность взять под опеку "
                                               " 'ваше животное'. Ваша поддержка может сделать мир лучше для них."
                                               " Спасибо, что приняли участие в нашей викторине "
                                               " и проявили интерес к животному миру. Вместе мы можем сделать больше! ",
                                               reply_markup=markup)


    elif message.text == 'Попробовать еще раз':
        try_again(message)


    elif message.text == 'Оставить отзыв':
        bot.send_message(message.from_user.id, "Пожалуйста, напишите свой отзыв:")
        bot.register_next_step_handler(message, gather_feedback)


    elif message.text == 'Овен необыкновенный ♈':
        user_id = message.from_user.id
        markup = types.InlineKeyboardMarkup()
        quiz_result = ("Поздравляю вас! Вам идеально подходит Сычуаньского Такина "
                       " - существо, которое символизирует устойчивость, адаптивность и силу. "
                       " Ваши уникальные качества, такие как способность преодолевать трудности, стойкость и упорство, "
                       " напоминают о такине, который бесстрашно бродит по горным склонам. "
                       " Ваша способность адаптироваться к любым обстоятельствам и найти свой путь, "
                       " даже в самых сложных ситуациях, вдохновляет и вызывает уважение. "
                       " Пусть Сычуаньский Такин будет вашим символом упорства и силы, "
                       " и пусть он всегда ведет вас по пути достижения ваших целей. "
                       " Поздравляю вас с этим уникальным сочетанием качеств и желаю, "
                       " чтобы ваша жизнь была полна достижений и успехов! ♈!!!")
        employee_id = id  # Здесь  ID Telegram сотрудника зоопарка
        send_telegram_message(employee_id, f"Пользователь {user_id} успешно прошел викторину")
        image_path = 'F:\Бот\Moscow3оо\images\kin.jpg'
        send_post(bot, message, image_path, quiz_result)
        facebook_share_link, vk_share_link = generate_share_links()
        btn1 = types.InlineKeyboardButton(text='СЫЧУАНЬСКИЙ ТАКИН ♈',
                                          url='https://moscowzoo.ru/animals/parnokopytnye/sychuanskiy-takin/?sphrase')
        btn2 = types.InlineKeyboardButton(text="Взять под опеку ❕", url='https://moscowzoo.ru/my-zoo/become-a-guardian/')
        btn_facebook = types.InlineKeyboardButton(" 🔲Поделиться в Facebook🔲", url=facebook_share_link)
        btn_vk = types.InlineKeyboardButton("🔲Поделиться в VK🔲", url=vk_share_link)
        markup.add(btn_facebook, btn1, btn2, btn_vk)
        bot.send_message(message.from_user.id, "Нажмите на кнопку 🔲, чтобы поделиться своим результатом или "
                                               " узнать больше о выбранном вами животном. "
                                               " Ведь каждое из них уникально и заслуживает нашего внимания."
                                               " Но помните, наши 'Братья меньшие' ℹ️ не всегда могут справиться "
                                               " без нашей помощи. Они нуждаются в защите и заботе, "
                                               " и каждый из нас может сделать свой вклад. 🆘"
                                               " Если вы чувствуете, что готовы подарить часть своего времени и любви "
                                               " этим удивительным созданиям, рассмотрите возможность взять под опеку "
                                               " 'ваше животное'. Ваша поддержка может сделать мир лучше для них."
                                               " Спасибо, что приняли участие в нашей викторине "
                                               " и проявили интерес к животному миру. Вместе мы можем сделать больше! ",
                                               reply_markup=markup)


    elif message.text == 'Попробовать еще раз':
        try_again(message)


    elif message.text == 'Оставить отзыв':
        bot.send_message(message.from_user.id, "Пожалуйста, напишите свой отзыв:")
        bot.register_next_step_handler(message, gather_feedback)


    elif message.text == 'Стрелец ♐':
        user_id = message.from_user.id
        markup = types.InlineKeyboardMarkup()
        quiz_result = ("Поздравляю! Вам отлично подходит ОВЦЕБЫК Овцебык обладает множеством замечательных качеств, "
                       " которые могут быть характерны и вам:"
                       " Выносливость: Овцебык известен своей способностью преодолевать сложности и преодолевать трудности."
                       " Оберегательство: Овцебык заботится о своих близких, "
                       " а его символом также является семейное благополучие."
                       " Умение адаптироваться: Овцебык легко адаптируется к переменам, "
                       " что является важным качеством в современном мире."
                       " Уравновешенность: Овцебык обладает спокойствием и уравновешенностью, "
                       " способными создавать гармонию во всем, что делает."
                       " Поздравляю вас! Эти качества могут прекрасно описывать вас, "
                       " и я желаю вам использовать их в полной мере для своего личного и профессионального роста.♐!")
        employee_id = id  # Здесь  ID Telegram сотрудника зоопарка
        send_telegram_message(employee_id, f"Пользователь {user_id} успешно прошел викторину")
        image_path = 'F:\Бот\Moscow3оо\images\ovce.jpg'
        send_post(bot, message, image_path, quiz_result)
        facebook_share_link, vk_share_link = generate_share_links()
        btn1 = types.InlineKeyboardButton(text='ОВЦЕБЫК ♐ ',
                                          url='https://moscowzoo.ru/animals/parnokopytnye/ovtsebyk/?sphrase')
        btn2 = types.InlineKeyboardButton(text="Взять под опеку ❕", url='https://moscowzoo.ru/my-zoo/become-a-guardian/')
        btn_facebook = types.InlineKeyboardButton(" 🔲Поделиться в Facebook🔲", url=facebook_share_link)
        btn_vk = types.InlineKeyboardButton("🔲Поделиться в VK🔲", url=vk_share_link)
        markup.add(btn_facebook, btn1, btn2, btn_vk)
        bot.send_message(message.from_user.id, "Нажмите на кнопку 🔲, чтобы поделиться своим результатом или "
                                               " узнать больше о выбранном вами животном. "
                                               " Ведь каждое из них уникально и заслуживает нашего внимания."
                                               " Но помните, наши 'Братья меньшие' ℹ️ не всегда могут справиться "
                                               " без нашей помощи. Они нуждаются в защите и заботе, "
                                               " и каждый из нас может сделать свой вклад. 🆘"
                                               " Если вы чувствуете, что готовы подарить часть своего времени и любви "
                                               " этим удивительным созданиям, рассмотрите возможность взять под опеку "
                                               " 'ваше животное'. Ваша поддержка может сделать мир лучше для них."
                                               " Спасибо, что приняли участие в нашей викторине "
                                               " и проявили интерес к животному миру. Вместе мы можем сделать больше! ",
                                               reply_markup=markup)


    elif message.text == 'Попробовать еще раз':
        try_again(message)


    elif message.text == 'Оставить отзыв':
        bot.send_message(message.from_user.id, "Пожалуйста, напишите свой отзыв:")
        bot.register_next_step_handler(message, gather_feedback)


    elif message.text == 'Стрелец v2.0 ♐':
        user_id = message.from_user.id
        markup = types.InlineKeyboardMarkup()
        quiz_result = ("Поздравляю вас! Вам идеально подходит Белохвостый Гну - непоколебимое и выносливое существо, "
                       " которое символизирует свободу и стойкость. Вы обладаете не только силой и выносливостью, "
                       " характерными для гну, но и умением стойко преодолевать преграды на своем пути. "
                       " Ваша энергия и решимость вдохновляют окружающих и позволяют вам добиваться поставленных целей. "
                       " Ваше присутствие наполняет пространство диким ветром свободы, "
                       " а ваше стремление к приключениям вдохновляет окружающих. "
                       " Позвольте Белохвостому Гну стать вашим символом стойкости и решительности, "
                       " и пусть он всегда будет вести вас по пути успеха и свободы. "
                       " Поздравляю вас с этим уникальным сочетанием качеств и желаю, "
                       " чтобы ваша жизнь была наполнена приключениями, радостью и свободой! ♐!!!")
        employee_id = id # Здесь  ID Telegram сотрудника зоопарка
        send_telegram_message(employee_id, f"Пользователь {user_id} успешно прошел викторину")
        image_path = 'F:\Бот\Moscow3оо\images\gnu.02.jpg'
        send_post(bot, message, image_path, quiz_result)
        facebook_share_link, vk_share_link = generate_share_links()
        btn1 = types.InlineKeyboardButton(text='БЕЛОХВОСТЫЙ ГНУ ♐',
                                          url='https://moscowzoo.ru/animals/parnokopytnye/belokhvostyy-gnu/?sphrase')
        btn2 = types.InlineKeyboardButton(text="Взять под опеку ❕", url='https://moscowzoo.ru/my-zoo/become-a-guardian/')
        btn_facebook = types.InlineKeyboardButton(" 🔲Поделиться в Facebook🔲", url=facebook_share_link)
        btn_vk = types.InlineKeyboardButton("🔲Поделиться в VK🔲", url=vk_share_link)
        markup.add(btn_facebook, btn1, btn2, btn_vk)
        bot.send_message(message.from_user.id, "Нажмите на кнопку 🔲, чтобы поделиться своим результатом или "
                                               " узнать больше о выбранном вами животном. "
                                               " Ведь каждое из них уникально и заслуживает нашего внимания."
                                               " Но помните, наши 'Братья меньшие' ℹ️ не всегда могут справиться "
                                               " без нашей помощи. Они нуждаются в защите и заботе, "
                                               " и каждый из нас может сделать свой вклад. 🆘"
                                               " Если вы чувствуете, что готовы подарить часть своего времени и любви "
                                               " этим удивительным созданиям, рассмотрите возможность взять под опеку "
                                               " 'ваше животное'. Ваша поддержка может сделать мир лучше для них."
                                               " Спасибо, что приняли участие в нашей викторине "
                                               " и проявили интерес к животному миру. Вместе мы можем сделать больше! ",
                                               reply_markup=markup)


    elif message.text == 'Попробовать еще раз':
        try_again(message)


    elif message.text == 'Оставить отзыв':
        bot.send_message(message.from_user.id, "Пожалуйста, напишите свой отзыв:")
        bot.register_next_step_handler(message, gather_feedback)


    elif message.text == 'Лев ♌':
        user_id = message.from_user.id
        markup = types.InlineKeyboardMarkup()
        quiz_result = ("Поздравляю вас!  Вы идеально соответствуете образу Индийского (Азиатского) Льва - существа, "
                       " символизирующего благородство, силу и мужество. "
                       " Ваша уверенность в себе и решительность, ваша способность вести и вдохновлять других, "
                       " ваша готовность защищать свои убеждения и ценности - все это делает "
                       " вас по-настоящему львиным лидером. Ваше присутствие внушает уважение и вызывает восхищение, "
                       " а ваша мудрость и сила духа служат примером для окружающих. "
                       " Позвольте Индийскому (Азиатскому) Льву стать вашим символом силы, мужества и благородства, "
                       " и пусть он всегда будет вести вас по пути успеха и достижений. "
                       " Поздравляю вас с этим уникальным сочетанием качеств и желаю, "
                       " чтобы ваша жизнь была наполнена смелостью, решительностью и благородством ♌!!!")
        employee_id = id # Здесь  ID Telegram сотрудника зоопарка
        send_telegram_message(employee_id, f"Пользователь {user_id} успешно прошел викторину")
        image_path = 'F:\Бот\Moscow3оо\images\leon.jpg'
        send_post(bot, message, image_path, quiz_result)
        facebook_share_link, vk_share_link = generate_share_links()
        btn1 = types.InlineKeyboardButton(text='ИНДИЙСКИЙ (АЗИАТСКИЙ) ЛЕВ ♌',
                                          url='https://moscowzoo.ru/animals/khishchnye/indiyskiy-aziatskiy-lev/?sphrase')
        btn2 = types.InlineKeyboardButton(text="Взять под опеку ❕", url='https://moscowzoo.ru/my-zoo/become-a-guardian/')
        btn_facebook = types.InlineKeyboardButton(" 🔲Поделиться в Facebook🔲", url=facebook_share_link)
        btn_vk = types.InlineKeyboardButton("🔲Поделиться в VK🔲", url=vk_share_link)
        markup.add(btn_facebook, btn1, btn2, btn_vk)
        bot.send_message(message.from_user.id, "Нажмите на кнопку 🔲, чтобы поделиться своим результатом или "
                                               " узнать больше о выбранном вами животном. "
                                               " Ведь каждое из них уникально и заслуживает нашего внимания."
                                               " Но помните, наши 'Братья меньшие' ℹ️ не всегда могут справиться "
                                               " без нашей помощи. Они нуждаются в защите и заботе, "
                                               " и каждый из нас может сделать свой вклад. 🆘"
                                               " Если вы чувствуете, что готовы подарить часть своего времени и любви "
                                               " этим удивительным созданиям, рассмотрите возможность взять под опеку "
                                               " 'ваше животное'. Ваша поддержка может сделать мир лучше для них."
                                               " Спасибо, что приняли участие в нашей викторине "
                                               " и проявили интерес к животному миру. Вместе мы можем сделать больше! ",
                                               reply_markup=markup)


    elif message.text == 'Попробовать еще раз':
        try_again(message)


    elif message.text == 'Назад в меню':
        handle_message(message)


    elif message.text == 'Оставить отзыв':
        bot.send_message(message.from_user.id, "Пожалуйста, напишите свой отзыв:")
        bot.register_next_step_handler(message, gather_feedback)







bot.polling(non_stop=True)
