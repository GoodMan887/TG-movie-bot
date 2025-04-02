import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

key_board_buttons = {
    'genre': '🎬Жанр',
    'top_3': '🏆Топ 3 фильма',
    'random_movie': '🪄Рандомный фильм'
}

buttons = [
    'Боевик',
    'Комедия',
    'Фантастика',
    'Фэнтези',
    'Триллер',
    'Ужасы',
    'Криминал',
    'Драма',
    'Мелодрама',
]
