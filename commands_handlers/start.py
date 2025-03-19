from telebot import TeleBot, types

import messages


def handle_command_start(message: types.Message, bot: TeleBot):
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True
    )
    markup.add('🎬Жанр', '🪄Рандомный фильм')
    bot.send_message(
        chat_id=message.chat.id,
        text=messages.start_message,
        reply_markup=markup
    )
