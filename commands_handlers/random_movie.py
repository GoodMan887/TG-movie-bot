from telebot import TeleBot, types

from database import postgresql_db


def handle_random_movie(message: types.Message, bot: TeleBot):
    """
    Обрабатывает команду юзера для выбора случайного фильма и отправляет его информацию.
    """
    movie = postgresql_db.get_random_movie()
    if not movie:
        bot.send_message(
            chat_id=message.chat.id,
            text="There's no movie"
        )
        return

    title, genre, time, rating, year, description, poster_url = movie
    response = (
        f"🎥 {title}\n"
        f"🗓️ {year}\n"
        f"⭐ {rating}\n"
        f"🍿 {genre}\n"
        f"⏱️ {time}\n\n"
        f"📝 {description}"
    )

    bot.send_photo(
        chat_id=message.chat.id,
        photo=poster_url,
        caption=response,
        parse_mode="Markdown",
    )
