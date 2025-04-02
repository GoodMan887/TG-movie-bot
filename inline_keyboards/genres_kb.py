from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

import config


def genre_kb():
    """Создаёт клавиатуру с кнопками для выбора жанра."""
    markup = InlineKeyboardMarkup()
    markup.add(*[InlineKeyboardButton(
        text=button,
        callback_data=f"genre_{button.lower()}") for button in config.buttons])
    return markup
