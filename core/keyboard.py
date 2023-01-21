from aiogram.types import *

start_inline=InlineKeyboardMarkup()
start_in1=InlineKeyboardButton(text="Site", url="https://rezka.ag/new")

start_inline.add(start_in1)

start_buttom=ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Новинка"),
    KeyboardButton("Рандомный фильм"),
    KeyboardButton("Все фильмы")
)

new_film=ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Показать новые 3 фильма"),
    KeyboardButton("Показать новые 5 фильма"),
    KeyboardButton("Показать новые 10 фильма "),
    KeyboardButton("Назад в меню")
)

# Admin_Button=ReplyKeyboardMarkup(resize_keyboard=True).add(
#     KeyboardButton("Обновить парсер")
# )

Admin_Button=InlineKeyboardMarkup(resize_keyboard=True).add(
InlineKeyboardButton("Обновить парсер", callback_data="admin_button")
)