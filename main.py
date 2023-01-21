import json
import random
from os import system
from time import sleep
from datetime import datetime

# Downloaded libraries - Скаченные библиотеки
import requests
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types import *

# Created module - Созданный модуль
from core.config import TOKEN, ADMIN_ALIBEK, ADMIN_ALIBEK_INT
from core.static.stickers import S001, S002
from core.keybord import start_inline, start_botom, new_film, Admin_botom
from core.rezka import rezka_parser


bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: Message):
    start_photo = ["core/static/image/images.png", "core/static/image/Без названия.jpeg", "core/static/image/Без названия (1).jpeg"]
    start_caption = f"""Привет <b>{message.from_user.last_name} {message.from_user.first_name}</b>. 
У нас есть все новинки кино за {datetime.now().strftime("%Y-%m-%d")}
    """
    await message.reply_photo(photo=open(random.choice(start_photo), "rb"), reply_markup=start_inline)
    await message.answer(text=start_caption, reply_markup=start_botom)

    if message.chat.id == ADMIN_ALIBEK_INT:
        await message.reply("Привет", reply_markup=Admin_botom)


@dp.message_handler(content_types=["text"])
async def message_text(message: Message):
    with open("core/all_kino.json", "r") as file:
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
<a href='{title_info["url"]}'>___ Ссылка на фильм ___</a>"""
            new_film_kino.append(text)

    if message.text.lower() == "новинка":
        await message.answer(text="Выберите сколько новых фильмов отправить", reply_markup=new_film)

    elif message.text.lower() in "3 фильма":
        await message.answer(new_film_kino[0])
        await message.answer(new_film_kino[1])
        await message.answer(new_film_kino[2])

    elif message.text.lower() in "5 фильмов":
        await message.answer(new_film_kino[0])
        await message.answer(new_film_kino[1])
        await message.answer(new_film_kino[2])
        await message.answer(new_film_kino[3])
        await message.answer(new_film_kino[4])
            
    elif message.text.lower() in "10 фильмов":
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

    elif message.text.lower() == "назад в меню":
        await message.reply("Вы в меню", reply_markup=start_botom)


    elif message.text.lower() == "рандомный фильм":
        await message.reply(random.choice(new_film_kino))


    elif message.text.lower() == "все фильмы":
        count = 0
        
        for i in new_film_kino:
            await message.reply(i)
            sleep(2)
            count += 1
            if count == 15:
                break
    else:
        await message.reply("Недоступная команда")

        
    # if message.text.lower == "обновить парсер":
    #     if message.chat.id == ADMIN_ALIBEK_INT:
    #         rezka_parser()
        
    #     else:
    #         await message.reply("Вам не сюда")

@dp.callback_query_handler(text="admin_botom")
async def send_random(call: types.CallbackQuery):
    rezka_parser()
    await call.message.answer("Подождите несколько секунд")

if __name__ == "__main__":
    executor.start_polling(dp)
