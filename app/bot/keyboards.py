from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder 

user = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Задать вопрос")
    ],
    [
        KeyboardButton(text="Редактировать профиль"),
        KeyboardButton(text="Настроить подписки")
    ]
],
    resize_keyboard=True,
    input_field_placeholder="Выбери действие"
)


lets_start = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Поехали", callback_data="insert_key")]
])



# Референс на будущее, вдруг понадобится (например, направления выбирать и прочее)
async def list_of_servers():
    servers = ['NL', 'FR', 'DE', 'RU', 'FI']

    keyboard = InlineKeyboardBuilder()
    for country in servers:
        keyboard.add(InlineKeyboardButton(text=country, callback_data=country))

    return keyboard.adjust(2).as_markup()