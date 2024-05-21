from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


start_keyboard =ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Начать ")],
    [KeyboardButton(text="Закончить")]
    ]
)

kb2 = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [InlineKeyboardButton(text="телеграм", url="https://t.me/GPT_chat_chatgpt_bot")],
        [InlineKeyboardButton(text="ютуб", url="youtube.com")],
        [InlineKeyboardButton(text="GitHub", url="https://github.com/Rinirasd")]
    ],resize_keyboard=True
)
items = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="телефон", callback_data="item_phone")],
        [InlineKeyboardButton(text="ноутбук", callback_data="item_laptop")],
        [InlineKeyboardButton(text="ВТ наушники", callback_data="item_headphones")]
    ]
)
