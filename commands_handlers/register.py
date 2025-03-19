from telebot import TeleBot

from commands_handlers.genre import handle_genre
from commands_handlers.start import handle_command_start


def register_start_command(bot: TeleBot):
    bot.register_message_handler(
        callback=handle_command_start,
        commands=['start'],
        pass_bot=True
    )

def register_genre_command(bot: TeleBot):
    bot.register_message_handler(
        callback=lambda message: handle_genre(message=message, bot=bot),
        func=lambda message: message.text == "🎬Жанр"
    )


def register_random_movie_command(bot: TeleBot):
    pass


def register_commands_handler(bot: TeleBot):
    register_start_command(bot)
    register_genre_command(bot)
