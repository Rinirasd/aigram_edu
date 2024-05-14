from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb =[
    [KeyboardButton(text="Кнопка 1 ")],
    [KeyboardButton(text="Кнопка 2 ")]
    ]
main = ReplyKeyboardMarkup(keyboard=kb)