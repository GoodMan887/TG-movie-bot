from telebot import TeleBot, types

import messages
from config import key_board_buttons


def handle_command_start(message: types.Message, bot: TeleBot):
    """
    Обработка команды start, отображение клавиатурных кнопок
    """
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True
    )
    markup.add(key_board_buttons['genre'], key_board_buttons['top_3'])
    markup.add(key_board_buttons['random_movie'])
    bot.send_message(
        chat_id=message.chat.id,
        text=messages.start_message,
        reply_markup=markup
    )
