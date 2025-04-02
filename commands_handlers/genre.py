import random

from telebot import TeleBot, types

from database import postgresql_db
from inline_keyboards.genres_kb import genre_kb
from inline_keyboards.choose_movie import this_or_another_movie
from messages import (
    good_watching,
    this_or_another,
    preference,
    choose,
    no_movie,
)


def handle_genre(message: types.Message, bot: TeleBot):
    """
    Обрабатывает сообщение с выбором жанра фильма.
    Отправляет сообщение с предложением выбрать жанр и отображает клавиатуру с кнопками жанров.
    """
    bot.send_message(
        chat_id=message.chat.id,
        text=preference
    )
    bot.send_message(
        chat_id=message.chat.id,
        text=choose,
        reply_markup=genre_kb()
    )


def callback_genre(query: types.CallbackQuery, bot: TeleBot):
    """
    Обрабатывает выбор жанра и отправляет юзеру случайный фильм выбранного жанра.
    """
    genre_name = query.data.split("_")[1]
    movies = postgresql_db.get_movies_by_genre(genre_name)
    if movies:
        movie = random.choice(movies)
        title, genre, time, rating, year, description, poster_url = movie
        response = (f"🎥 {title}\n"
                    f"🗓️ {year}\n"
                    f"⭐ {rating}\n"
                    f"🍿 {genre}\n"
                    f"⏱️ {time}\n\n"
                    f"📝 {description}")

        bot.send_photo(
            chat_id=query.message.chat.id,
            photo=poster_url,
            caption=response,
            parse_mode="Markdown",
        )
        bot.send_message(
            chat_id=query.message.chat.id,
            text=this_or_another,
            reply_markup=this_or_another_movie(genre_name)
        )
    else:
        bot.send_message(
            chat_id=query.message.chat.id,
            text=no_movie
        )


def handle_movie_choice(query: types.CallbackQuery, bot: TeleBot):
    """
    Обрабатывает выбор юзера после рекомендации фильма:
    - Если юзер выбрал "Да", отправляет сообщение с пожеланием приятного просмотра.
    - Если юзер выбрал "Давай другой", отправляет новый фильм того же жанра.
    """
    choice, genre_name = query.data.split('_', 1)
    if choice == 'watch':
        bot.send_message(
            chat_id=query.message.chat.id,
            text=good_watching
        )
    elif choice == 'another':
        movies = postgresql_db.get_movies_by_genre(genre_name)
        if movies:
            movie = random.choice(movies)
            title, genre, time, rating, year, description, poster_url = movie
            response = (f"🎥 {title}\n"
                        f"🗓️ {year}\n"
                        f"⭐ {rating}\n"
                        f"🍿 {genre}\n"
                        f"⏱️ {time}\n\n"
                        f"📝 {description}")

            bot.send_photo(
                chat_id=query.message.chat.id,
                photo=poster_url,
                caption=response,
                parse_mode="Markdown",
            )
            bot.send_message(
                chat_id=query.message.chat.id,
                text=this_or_another,
                reply_markup=this_or_another_movie(genre_name)
            )
        else:
            bot.send_message(
                chat_id=query.message.chat.id,
                text="There's no movie"
            )
