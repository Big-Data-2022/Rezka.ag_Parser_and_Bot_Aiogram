from aiogram.types import *

start_inline = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text="Site", url="https://rezka.ag/new")
)

start_button = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Новинка"), 
    KeyboardButton("Рандомная новинка"), 
    KeyboardButton("Все фильмы")
)

# Новинка
new_film = ReplyKeyboardMarkup(resize_keyboard = True).add(
    KeyboardButton("3 фильма"),
    KeyboardButton("5 фильма"),
    KeyboardButton("10 фильма"),
    KeyboardButton("Назад в меню"),
    
    )

# ADMIN_BUTTON = ReplyKeyboardMarkup(resize_keyboard = True).add(
#     KeyboardButton("Обновить парсера"),
# )


ADMIN_BUTTON = InlineKeyboardMarkup().add(
    InlineKeyboardButton("Обновить парсер", callback_data = "admin_button"),
)


