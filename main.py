import json
import pytz
import random
from os import system
from time import sleep
from datetime import datetime


from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types import *

# Created module - Созданный модуль
from core.config import TOKEN, ADMIN_ID
from core.static.stiker import S002
from core.keyboard import start_inline, start_buttom, new_film, Admin_Button

from core.rezka import rezka_parser
bot=Bot(token=TOKEN, parse_mode="HTML")


dp=Dispatcher(bot)

system("clear")
@dp.message_handler(commands=["start"])
async def start(message: Message):
    start_photo=["core/static/image/18520.jpg","core/static/image/cityscape-street-photography-ir.jpg","core/static/image/city-road-night-lights.jpg"]
    start_caption=f"""Hello <b>{message.from_user.first_name}</b>"""

    await message.reply_photo(open(random.choice(start_photo), "rb"), caption=start_caption, reply_markup=start_inline)
    await message.answer(f"У нас есть самые новые фильмы {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", reply_markup=start_buttom)
    
    if message.chat.id==ADMIN_ID:
        await message.reply("Hello my God",reply_markup=Admin_Button)




@dp.message_handler(content_types=["text"])
async def message_text(message: Message):
    with open("core/json/all_inf.json", "r")as file:
        all_kino=json.load(file)
    new_film_kino=[]
    for i in all_kino:
        for j in i.items():
            title=j[0]
            title_info=j[1]
            text=f"""
Название:{title}
Жанр:{title_info["description"].split(",")[-1]}
Страна:{title_info["description"].replace("-",",").split(",")[-2]}
Год выпуска:{title_info["description"].replace("-",",").split(",")[-3]}
<a href='{title_info["url"]}'>Ссылка на фильм</a>
            """
            new_film_kino.append(text)



    
    
    if message.text.lower()=="новинка":
        await message.answer(text="Выберите сколько новых фильмов отправить", reply_markup=new_film)
    elif message.text.lower() == "показать новые 3 фильма":
            await message.answer(text=new_film_kino[0])
            await message.answer(text=new_film_kino[1])
            await message.answer(text=new_film_kino[2])
    elif message.text.lower()== "показать новые 5 фильма":
            await message.answer(text=new_film_kino[0])
            await message.answer(text=new_film_kino[1])
            await message.answer(text=new_film_kino[2])
            await message.answer(text=new_film_kino[3])
            await message.answer(text=new_film_kino[4])    
    elif message.text.lower() == "показать новые 10 фильма":
            await message.answer(text=new_film_kino[0])
            await message.answer(text=new_film_kino[1])
            await message.answer(text=new_film_kino[2])
            await message.answer(text=new_film_kino[3])
            await message.answer(text=new_film_kino[4])
            await message.answer(text=new_film_kino[5])
            await message.answer(text=new_film_kino[6])
            await message.answer(text=new_film_kino[7])
            await message.answer(text=new_film_kino[8])
            await message.answer(text=new_film_kino[9])

    elif message.text.lower() == "назад в меню":
        await message.reply("Вы в меню", reply_markup=start_buttom)


    elif message.text.lower() == "рандомный фильм":
        await message.reply(random.choice(new_film_kino))

    elif message.text.lower() == "все фильмы":
        count=0
        for i in new_film_kino:
            await message.reply(i)
            sleep(4)
            count+=1
            if count == 10:
                break
    else:
        await message.reply("Не доступная команда")

    
 

@dp.callback_query_handler(text="admin_bottom")
async def send_random_value(call: CallbackQuery):
    await call.message.answer("Ны тыкайте идет обновление")
    rezka_parser()
    await call.message.answer("Обновление парсера,подождите")

if __name__ == '__main__':
    executor.start_polling(dp)
