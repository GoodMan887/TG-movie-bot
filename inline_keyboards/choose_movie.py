from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

from messages import movie_msg


def this_or_another_movie(genre_name):
    """Создаёт клавиатуру с кнопками для выбора фильма или другого в таком же жанре."""
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton(
        movie_msg[0], callback_data=f'watch_{genre_name}'
    )
    button_2 = InlineKeyboardButton(
        movie_msg[1], callback_data=f'another_{genre_name}'
    )

    markup.add(button_1, button_2)
    return markup
