from aiogram.types import *

start_inline = InlineKeyboardMarkup(row_width=3)
start_in_1 = InlineKeyboardButton(text="rezka.ag", url="https://rezka.ag/new/")
start_in_2 = InlineKeyboardButton(text="GitHub", url="https://github.com/mikonaft")
start_in_3 = InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/mikonaft/")
start_inline.add(start_in_1, start_in_2, start_in_3)

start_button = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('новинки'),
    KeyboardButton('случайный фильм'),
    KeyboardButton('все фильмы')
)

new_film = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('новые 3 фильма'),
    KeyboardButton('новые 5 фильмов'),
    KeyboardButton('новые 10 фильмов'),
    KeyboardButton('назад в меню'),
)

# ADMIN_BUTTON = ReplyKeyboardMarkup(resize_keyboard=True).add(
#     KeyboardButton('обновить парсер')
# )

ADMIN_BUTTON = InlineKeyboardMarkup().add(
    InlineKeyboardButton('обновить парсер', callback_data='admin_button')
)