from aiogram.types import *

start_inline = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text="Site", url="https://rezka.ag/new")
)

start_button = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Новинка"), 
    KeyboardButton("Рандомный Фильм"), 
    KeyboardButton("Все фильмы")
)

# Новинка
new_film = ReplyKeyboardMarkup(resize_keyboard = True).add(
    KeyboardButton("Показать новые 3 фильма"),
    KeyboardButton("Показать новые 5 фильма"),
    KeyboardButton("Показать новые 10 фильма"),
    KeyboardButton("Назад в меню"),
    
    )

# ADMIN_BUTTON = ReplyKeyboardMarkup(resize_keyboard = True).add(
#     KeyboardButton("Обновить парсера"),
# )


ADMIN_BUTTON = InlineKeyboardMarkup().add(
    InlineKeyboardButton("Обновить парсера", callback_data = "admin_button"),
)


