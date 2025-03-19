import random
from telebot import (
    types,
    TeleBot,
)

from data_base import postgresql_db


def callback_genre(query: types.CallbackQuery, bot: TeleBot):
    genre_name = query.data.split("_")[1]
    movies = postgresql_db.get_movies_by_genre(genre_name)
    print(genre_name)
    print(movies)
    if movies:
        movie = random.choice(movies)
        title, rating, year, description, poster_url = movie
        response = f"🎬 {title} ({year}) - ⭐ {rating}\n\n_{description}_-"

        bot.send_photo(
            chat_id=query.message.chat.id,
            photo=poster_url,
            caption=response,
            parse_mode="Markdown",
        )
    else:
        bot.send_message(
            chat_id=query.message.chat.id,
            text="There's no movie"
        )


def register_callback_genre(bot: TeleBot):
    bot.register_callback_query_handler(
        lambda query: callback_genre(query, bot),
        lambda query: query.data.startswith('genre_'),
    )
