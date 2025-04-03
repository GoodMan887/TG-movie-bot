from telebot import TeleBot

import config
import keep_alive
from commands_handlers.register import (register_callback_query,
                                        register_commands_handler)

bot = TeleBot(config.BOT_TOKEN)


def register_handlers():
    register_commands_handler(bot)
    register_callback_query(bot)


register_handlers()


if __name__ == '__main__':
    keep_alive.keep_alive()
    bot.infinity_polling(skip_pending=True)
