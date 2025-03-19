from telebot import TeleBot

import config
from commands_handlers.register import register_commands_handler
from data_base.callback_handler_of_genres import register_callback_genre

bot = TeleBot(config.BOT_TOKEN)


def register_handlers():
    register_commands_handler(bot)
    register_callback_genre(bot)


register_handlers()


if __name__ == '__main__':
    bot.infinity_polling(skip_pending=True)
