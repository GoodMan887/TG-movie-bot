from telebot import TeleBot, types

from keyboards.genres_kb import genre_kb


def handle_genre(message: types.Message, bot: TeleBot):
    bot.send_message(
        chat_id=message.chat.id,
        text="Хочешь посмеяться, испугаться, или поплакать?"
    )
    bot.send_message(
        chat_id=message.chat.id,
        text='Выбирай:',
        reply_markup=genre_kb()
    )
