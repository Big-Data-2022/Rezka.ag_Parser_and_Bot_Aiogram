from aiogram.types import *

start_inline = InlineKeyboardMarkup()
start_inline.add(
    InlineKeyboardButton(text="site", url="https://rezka.ag/new"),
    InlineKeyboardButton(text="vk", url="https://vk.com/luvvviss"),
    InlineKeyboardButton(text="discord", url="https://discord.gg/AbEwgjBd"),
)

start_button = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Новинка"), 
    KeyboardButton("Рандомный фильм"),
    KeyboardButton("Все фильмы")
)

#Novinka
new_filme = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Показать новые 3 фильма"),
    KeyboardButton("Показать новые 5 фильмов"),
    KeyboardButton("Показать новые 10 фильмов"),
    KeyboardButton("Назад в меню")
)

# ADMIN_BUTTON = ReplyKeyboardMarkup(resize_keyboard=True).add(
#     KeyboardButton("Обновить парсера")
# )

ADMIN_BUTTON = InlineKeyboardMarkup().add(
    InlineKeyboardButton("Обновить парсер", callback_data="admin_button")
)