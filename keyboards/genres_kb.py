from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
# from config import callback_data_buttons


def genre_kb():
    markup = InlineKeyboardMarkup()
    markup.add(*[InlineKeyboardButton(
        text=button,
        callback_data=f"genre_{button}") for button in config.buttons])
    return markup
