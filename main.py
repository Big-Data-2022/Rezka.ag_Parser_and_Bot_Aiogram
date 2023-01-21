# Default modules - Модули по умолчанию
import json
import pytz
import random
from os import system
from time import sleep
from datetime import datetime

# Downloaded libraries - Скаченные библиотеки
from aiogram import Bot
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types import *

# Created module - Созданный модуль
from core.config import TOKEN, ADMIN_ID_INT
# from core.static.stikers import S001
from core.keyboard import start_inline, start_button, new_film, ADMIN_BUTTON
from core.rezka import rezka_parser

system('clear')
bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: Message):
    start_photo = ["core/static/image/start.jpg","core/static/image/start2.jpg"]
    start_caption = f"Добро пожаловать <b>{message.from_user.first_name}</b>! \nТебе нравится смотреть кино дома? Привык после работы или учебы, приходя домой, сразу же включать телевизор или ноутбук? Не хочешь посещать кинотеатр, но и от новых фильмов не готов отказаться? Это вовсе не беда!"
    await message.reply_photo(photo=open(random.choice(start_photo), "rb"), caption=start_caption, reply_markup=start_inline)
    await message.answer(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} \nВ нашем телеграм боте вы найдете самые новые фильмы, сериалы!", reply_markup=start_button)

    if message.chat.id == ADMIN_ID_INT:
        await message.reply("Привет, хозяин", reply_markup=ADMIN_BUTTON) 

@dp.message_handler(content_types=["text"])
async def message_text(message: Message):
    with open("core/json/rezka.json", "r") as file:
        all_kino = json.load(file)

    new_film_kino = []
    for i in all_kino:
        for j in i.items():
            title = j[0]
            title_info = j[1]
            text = f"""
Название: {title}
Жанр: {title_info["description"].split(",")[-1]}
Страна: {title_info["description"].replace("-", ",").split(",")[-2]}
Год выпуска: {title_info["description"].replace("-", ",").split(",")[-3]}
<a href='{title_info["url"]}'>Ссылка на фильм </a>"""
            new_film_kino.append(text)

    if message.text.lower() == "новинка":
        await message.answer(text="Выберите сколько новых фильмов отправить", reply_markup=new_film)
    elif message.text.lower() in "3 фильма":
        await message.answer(new_film_kino[0])
        await message.answer(new_film_kino[1])
        await message.answer(new_film_kino[2])
    elif message.text.lower() in "5 фильма":
        await message.answer(new_film_kino[0])
        await message.answer(new_film_kino[1])
        await message.answer(new_film_kino[2])
        await message.answer(new_film_kino[3])
        await message.answer(new_film_kino[4])
    elif message.text.lower() in "10 фильма":
        await message.answer(new_film_kino[0])
        await message.answer(new_film_kino[1])
        await message.answer(new_film_kino[2])
        await message.answer(new_film_kino[3])
        await message.answer(new_film_kino[4])
        await message.answer(new_film_kino[5])
        await message.answer(new_film_kino[6])
        await message.answer(new_film_kino[7])
        await message.answer(new_film_kino[8])
        await message.answer(new_film_kino[9])
        await message.answer(new_film_kino[10])
    elif message.text.lower() == "назад в меню":
        await message.reply("Вы в меню", reply_markup = start_button)

    elif message.text.lower() == "рандомная новинка":
        await message.reply(random.choice(new_film_kino))
    
    elif message.text.lower() == "все фильмы":
        count = 0 

        for i in new_film_kino:
            await message.reply(i)
            sleep(6)
            count += 1
            if count == 20:
                break
    # if message.text.lower() == "обновить парсер":
    #     if message.chat.id == ADMIN_ID_INT:
    #         rezka_parser()

    else:
        await message.reply("Недоступная команда")

@dp.callback_query_handler(text = "admin_button") 
async def send_random_value(call: CallbackQuery):
    await call.message.answer("Подождите, идет обновление")
    rezka_parser()
    await call.message.answer("Обновлен <b>json file</b>")

if __name__ == "__main__":
    print("Welcome")
    executor.start_polling(dp)




# Тебе нравится смотреть кино дома? Привык после работы или учебы, приходя домой, сразу же включать телевизор или компьютер? Не хочешь посещать кинотеатр, но и от новых фильмов не готов отказаться? Это вовсе не беда! Главное найти приятное положительное решение - предлагаем тебе смотреть фильмы в HD онлайн бесплатно на данной странице! Все лучшие 


# Картинка: {title_info["photo"]}
