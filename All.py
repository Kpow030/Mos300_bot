import telebot
import os
import random
import webbrowser
import urllib.parse
import requests
import vk_api
import telegram



from telegram import Bot
from telebot import types


bot = telebot.TeleBot("TOKEN")

TOKEN = "TOKEN"

links = ['https://moscowzoo.ru/animals/sokoloobraznye/grif/?sphrase_id=737599',
        'https://moscowzoo.ru/animals/popugaeobraznye/malyy-soldatskiy-ara/?sphrase_id=737595',
        'https://moscowzoo.ru/animals/aistoobraznye/alyy-ili-krasnyy-ibis/?sphrase_id=737597',
        'https://moscowzoo.ru/animals/sovoobraznye/dlinnokhvostaya-neyasyt/?sphrase_id=737598',
        'https://moscowzoo.ru/animals/pingvinoobraznye/yuzhnoafrikanskiy-ili-ochkovyy-pingvin/?sphrase_id=737596',
        'https://moscowzoo.ru/animals/aistoobraznye/krasnoshchekiy-ibis/?sphrase_id=741225',
        'https://moscowzoo.ru/animals/aistoobraznye/chernyy-aist/?sphrase_id=741223',
        'https://moscowzoo.ru/animals/skorpenoobraznye/mombasskaya-krylatka/?sphrase_id=737797',
        'https://moscowzoo.ru/animals/okuneobraznye/anemonovaya-ryba-lozhnyy-kloun/?sphrase',
        'https://moscowzoo.ru/animals/cheshuichatye/obyknovennaya-iguana/?sphrase',
        'https://moscowzoo.ru/animals/cherepakhi/slonovaya-cherepakha/?sphrase_id=737800',
        'https://moscowzoo.ru/animals/krokodily/gavialovyy-krokodil/?sphrase_id=737802',
        'https://moscowzoo.ru/animals/khishchnye/kamyshovyy-kot/?sphrase_id=738172',
        'https://moscowzoo.ru/animals/primaty/zolotistyy-tamarin/?sphrase',
        'https://moscowzoo.ru/animals/khishchnye/kamyshovyy-kot/?sphrase_id=738172',
        'https://moscowzoo.ru/animals/khishchnye/kharza/?sphrase',
        'https://moscowzoo.ru/animals/neparnokopytnye/loshad-przhevalskogo/?sphrase',
        'https://moscowzoo.ru/animals/nepolnozubye/sharovidnyy-bronenosets/?sphrase',
        'https://moscowzoo.ru/animals/parnokopytnye/dagestanskiy-vostochnokavkazskiy-tur/?sphrase',
        'https://moscowzoo.ru/animals/parnokopytnye/sychuanskiy-takin/?sphrase',
        'https://moscowzoo.ru/animals/parnokopytnye/ovtsebyk/?sphrase',
        'https://moscowzoo.ru/animals/parnokopytnye/belokhvostyy-gnu/?sphrase',
        'https://moscowzoo.ru/animals/khishchnye/indiyskiy-aziatskiy-lev/?sphrase',
        'https://moscowzoo.ru/animals/sovoobraznye/splyushka/?sphrase_id=741226',
         ]




registered_users = {}


def send_quiz_success_message(user_id):
    message = f"Пользователь с id {user_id} успешно прошел викторину"
    bot.send_message(chat_id=1932614138, text=message)



def send_telegram_message(employee_id, message):
    bot.send_message(employee_id, message)

def send_message_to_zoo_employee(message):
    return "Сообщение о прохождении викторины, успешно отправлено сотруднику зоопарка!"



def open_random_link(links):
    link = random.choice(links)
    return link




def upload_image_to_social_network(image_path):
    image_url = "https://example.com/image.jpg"
    return image_url




def send_post(bot, message, image_path, quiz_result):
    post_text = f"{quiz_result}\n"
    markup = types.InlineKeyboardMarkup()
    facebook_share_link, vk_share_link = generate_share_links()
    btn_facebook = types.InlineKeyboardButton("Поделиться в Facebook", url=facebook_share_link)
    btn_vk = types.InlineKeyboardButton("Поделиться в VK", url=vk_share_link)
    markup.add(btn_facebook, btn_vk)

    with open(image_path, "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption=post_text)




def generate_share_links():
    facebook_share_link = "https://example.com/share/facebook"
    vk_share_link = "https://example.com/share/vk"
    return facebook_share_link, vk_share_link




def gather_feedback(message):
    feedback = message.text
    with open('feedback.txt', 'a', encoding='utf-8') as file:
        file.write(feedback + '\n')
    print("Спасибо за ваш отзыв!")



@bot.message_handler(content_types=['text'])
def try_again(message):
    if message.text == 'Попробовать еще раз':
        bot.send_message(message.chat.id, 'Спасибо огромное что приняли участие в нашей викторине')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key = types.KeyboardButton("🏁Хочу участвовать")
        key1 = types.KeyboardButton("⛔Не хочу участвовать")
        markup.add(key, key1)
        bot.send_message(message.chat.id, " Давайте посмотрим какие животные есть под другими ответами?",
                        reply_markup=markup)

    elif message.text == '🏁Хочу участвовать':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Выводятся после согласия
        m = types.KeyboardButton('Воздух 💨')
        m1 = types.KeyboardButton('Земля 🌎')
        m2 = types.KeyboardButton('Огонь 🔥')
        m3 = types.KeyboardButton('Вода 💧')
        markup.add(m, m1, m2, m3)
        bot.send_message(message.from_user.id,
                         'Выберите наиболее подходящую вам стихию', reply_markup=markup)



    elif message.text == '⛔Не хочу участвовать':
        link = open_random_link(links)
        response = f"Очень жаль, что вы отказываетесь. Мы будем вас ждать снова🆘"
        markup = types.InlineKeyboardMarkup()
        b = types.InlineKeyboardButton(text="Открыть ссылку", url=link)
        markup.add(b)
        bot.send_message(message.from_user.id, response, reply_markup=markup)




@bot.message_handler(content_types=['text'])
def handle_message(message):
    if message.text == 'Назад в меню':
        bot.send_message(message.chat.id, "👋 Я надеюсь у меня получится Вас переубедить")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mr = types.KeyboardButton("🏁Хочу участвовать")
        mr1 = types.KeyboardButton("⛔Не хочу участвовать")
        markup.add(mr, mr1)
        bot.send_message(message.chat.id, "Вы так рано уходите? Викторина еще не закончилась"
                                      " Я задам вам пару вопросов. По результатам ответов я познакомлю Вас с"
                                      " вашим новым другом 🆘📕",
                                        reply_markup=markup)


    elif message.text == '🏁Хочу участвовать':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Выводятся после согласия
        ma = types.KeyboardButton('Воздух 💨')
        ma1 = types.KeyboardButton('Земля 🌎')
        ma2 = types.KeyboardButton('Огонь 🔥')
        ma3 = types.KeyboardButton('Вода 💧')
        markup.add(ma, ma1, ma2, ma3)
        bot.send_message(message.from_user.id,
                         'Выберите наиболее подходящую вам стихию', reply_markup=markup)

    elif message.text == '⛔Не хочу участвовать':
        link = open_random_link(links)
        response1 = f"Очень жаль, что вы отказываетесь. Ведь я нуждаюсь в вашей помощи 🆘"
        markup = types.InlineKeyboardMarkup()
        bn1 = types.InlineKeyboardButton(text="Открыть ссылку", url=link)
        markup.add(bn1)
        bot.send_message(message.from_user.id, response1, reply_markup=markup)



