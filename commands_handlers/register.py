"""Регистрация обработчиков для команд и колбеков бота,
   включая обработку сообщений, отправленных через клавиатурные кнопки."""

from functools import partial

from telebot import TeleBot

from commands_handlers.genre import (callback_genre, handle_genre,
                                     handle_movie_choice)
from commands_handlers.random_movie import handle_random_movie
from commands_handlers.start import handle_command_start
from commands_handlers.top_3_movies import handle_top_movies
from config import key_board_buttons


def register_start_command_handler(bot: TeleBot):
    bot.register_message_handler(
        callback=handle_command_start,
        commands=['start'],
        pass_bot=True
    )


# Выдача инлайн кнопок при нажатии клавиатурной кнопки "Жанр"
def register_genre_message_handler(bot: TeleBot):
    bot.register_message_handler(
        callback=lambda message: handle_genre(message=message, bot=bot),
        func=lambda message: message.text == key_board_buttons['genre']
    )


def register_genre_callback_handler(bot: TeleBot):
    bot.register_callback_query_handler(
        lambda query: callback_genre(query, bot),
        lambda query: query.data.startswith('genre_'),
    )


def register_movie_choice_callback_handler(bot: TeleBot):
    bot.register_callback_query_handler(
        partial(handle_movie_choice, bot=bot),
        lambda query: query.data.startswith('watch') or
                      query.data.startswith('another')
    )


def register_top_movies_message_handler(bot: TeleBot):
    bot.register_message_handler(
        partial(handle_top_movies, bot=bot),
        func=lambda message: message.text == key_board_buttons['top_3']
    )


def register_random_movie_message_handler(bot: TeleBot):
    bot.register_message_handler(
        partial(handle_random_movie, bot=bot),
        func=lambda message: message.text == key_board_buttons['random_movie']
    )


def register_commands_handler(bot: TeleBot):
    """Регистрирует команды бота (текстовые команды)."""
    register_start_command_handler(bot)
    register_genre_message_handler(bot)
    register_random_movie_message_handler(bot)
    register_top_movies_message_handler(bot)


def register_callback_query(bot: TeleBot):
    """Регистрирует callback-запросы (обработчики нажатий inline-кнопок)."""
    register_genre_callback_handler(bot)
    register_movie_choice_callback_handler(bot)
