from telebot import TeleBot, types

from database import postgresql_db
from messages import top_movies_msg


def handle_top_movies(message: types.Message, bot: TeleBot):
    """
    Обрабатывает сообщение топ-3 фильма и отправляет 3 фильма с рейтингом >= 7.0.
    """
    movies = postgresql_db.get_top_3_movies()
    if movies:
        for movie in movies:
            title, genre, time, rating, year, description, poster_url = movie
            response = (f"🎥 {title}\n"
                        f"🗓️ {year}\n"
                        f"⭐ {rating}\n"
                        f"🍿 {genre}\n"
                        f"⏱️ {time}\n\n"
                        f"📝 {description}")

            bot.send_photo(
                chat_id=message.chat.id,
                photo=poster_url,
                caption=response,
                parse_mode="Markdown",
            )
        bot.send_message(
            chat_id=message.chat.id,
            text=top_movies_msg,
        )
    else:
        bot.send_message(
            chat_id=message.chat.id,
            text="There's no movie"
        )
