from aiogram.types import *

start_inline = InlineKeyboardMarkup()

ikb1 = InlineKeyboardButton(text="Site", url="https://rezka.ag/new/")
ikb2 = InlineKeyboardButton(text="ITC", url="https://www.itcbootcamp.com/#/")
ikb3 = InlineKeyboardButton(text="Film", url="https://ru.wikipedia.org/wiki/%D0%A4%D0%B8%D0%BB%D1%8C%D0%BC")

start_inline.add(ikb1, ikb2, ikb3)



start_botom = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Новинка"), KeyboardButton("Рандомный фильм"), KeyboardButton("Все фильмы")
)

new_film = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("3 фильма"), KeyboardButton("5 фильмов"),
    KeyboardButton("10 фильмов"), KeyboardButton("Назад в меню")
)

# admin_botom = ReplyKeyboardMarkup(resize_keyboard=True).add(
#     KeyboardButton("Обновить парсер")
# )
Admin_botom = InlineKeyboardMarkup().add(
    InlineKeyboardButton("Обновить парсер", callback_data="admin_botom")
)

