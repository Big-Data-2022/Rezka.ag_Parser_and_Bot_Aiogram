# default modules
import json
import random
from os import system
from time import sleep
from datetime import datetime

#download modules
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from aiogram.types import * 

#created modules
from core.config import TOKEN_API, ADMIN_ID, ADMIN_ID_INT
#from core.static.stikers import S001, S002
from core.keyboard import start_inline, start_button, new_film, ADMIN_BUTTON
from core.rezka import rezka_parser
bot = Bot(token=TOKEN_API, parse_mode='HTML')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    start_photo = ['core/static/image/img1.jpg', 'core/static/image/img2.jpg', 'core/static/image/img3.jpg']
    start_caption = f"Привет, <b>{message.from_user.first_name}</b>!"
    await message.answer_photo(photo=open(random.choice(start_photo), 'rb'), caption=start_caption, reply_markup=start_inline)
    await message.answer(text=f"В нашем боте ты найдешь самые новые фильмы! На сегодня {datetime.now().strftime('%Y-%m-%d')}", reply_markup=start_button)
    if message.chat.id == ADMIN_ID_INT:
        await message.reply("Приветствую Владыка", reply_markup=ADMIN_BUTTON)
        



@dp.message_handler(content_types=['text'])
async def message_text(message: types.Message):
    with open("core/json/rezka.json", "r") as file:
        all_kino = json.load(file)
        
    new_films_info = []
    for i in all_kino:
        for j in i.items():
            title = j[0]
            title_info = j[1]
            text = f"""
Название: {title}
Жанр: {title_info['description'].split(',')[-1]}
Страна: {title_info['description'].replace('-', ',').split(',')[-2]}
Год выпуска: {title_info['description'].replace('-', ',').split(',')[-3]}
<a href='{title_info['url']}'> ---ссылка на фильм--- </a>
            """
            new_films_info.append(text)
            
    if message.text.lower() == 'новинки':
        await message.answer('выберите сколько фильмов вы хотите получить', reply_markup=new_film)
    elif message.text.lower() == 'новые 3 фильма':
        await message.answer(new_films_info[0])
        await message.answer(new_films_info[1])
        await message.answer(new_films_info[2])
    elif message.text.lower() == 'новые 5 фильмов':
        await message.answer(new_films_info[0])
        await message.answer(new_films_info[1])
        await message.answer(new_films_info[2])          
        await message.answer(new_films_info[3])          
        await message.answer(new_films_info[4])
    elif message.text.lower() == 'новые 10 фильмов':
        await message.answer(new_films_info[0])
        await message.answer(new_films_info[1])
        await message.answer(new_films_info[2])          
        await message.answer(new_films_info[3])          
        await message.answer(new_films_info[4])
        await message.answer(new_films_info[5])
        await message.answer(new_films_info[6])
        await message.answer(new_films_info[7])          
        await message.answer(new_films_info[8])          
        await message.answer(new_films_info[9])   
    elif message.text.lower() == 'назад в меню':
        await message.reply('вы вернулись в главное меню', reply_markup=start_button)      
        
    elif message.text.lower() == 'случайный фильм':
        await message.reply(random.choice(new_films_info))

    elif message.text.lower() == 'все фильмы':
        count = 0
        for i in new_films_info:
            await message.reply(i)
            sleep(6)
            count += 1
            if count == 20:
                break
    else:
        await message.answer(f"Неизвестная команда {message.text}")
        
    # if message.text.lower() == 'обновить парсер':
    #     if message.chat.id == ADMIN_ID_INT:
    #         rezka_parser()
    #     else:
    #         await message.reply('ДОСТУП ЗАПРЕЩЕН!!!!')
        
@dp.callback_query_handler(text='admin_button')
async def send_random_value(call: CallbackQuery):
    await call.message.answer('please wait...')
    rezka_parser()
    await call.message.answer('films updated <b>begin</b>')

if __name__ == '__main__':
    print('Bot started!')
    executor.start_polling(dp)