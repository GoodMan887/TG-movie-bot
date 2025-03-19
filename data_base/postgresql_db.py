import os

import psycopg2
from dotenv import load_dotenv

# Перенос переменных из .env (не работает)
# env = environ.Env(
#     DATABASE_NAME=str,
#     DATABASE_USER=str,
#     DATABASE_PASSWORD=str,
#     DATABASE_HOST=str,
#     DATABASE_PORT=str,
# )
# environ.Env.read_env()

# def connect_db():
#     return psycopg2.connect(
#     dbname=env.str("DATABASE_NAME"),
#     user=env.str("DATABASE_USER"),
#     password=env.str("DATABASE_PASSWORD"),
#     host=env.str("DATABASE_HOST"),
#     port=env.int("DATABASE_PORT")
#     )

# print('DATABASE_NAME:', env('DATABASE_NAME', default="Not found"))
# print('DATABASE_USER:', env('DATABASE_USER', default="Not found"))
# print('DATABASE_PASSWORD:', env('DATABASE_PASSWORD', default="Not found"))
# print('DATABASE_HOST:', env('DATABASE_HOST', default="Not found"))
# print('DATABASE_PORT:', env('DATABASE_PORT', default="Not found"))

load_dotenv()

# Подключение к базе через переменные окружения из ОС
def connect_db():
    return psycopg2.connect(
    dbname=os.getenv("DATABASE_NAME"),
    user=os.getenv("DATABASE_USER"),
    password=os.getenv("DATABASE_PASSWORD"),
    host=os.getenv("DATABASE_HOST"),
    port=os.getenv("DATABASE_PORT")
    )


# Функция для получения списка жанров
def get_genres():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM genres;")
    genres = cursor.fetchall()
    cursor.close()
    conn.close()
    return genres


# Функция для получения фильмов по жанру
def get_movies_by_genre(genre_name):
    conn = connect_db()
    cursor = conn.cursor()
    query = """
        SELECT movies.title, movies.rating, movies.year, movies.description, movies.poster_url FROM movies
        JOIN genres ON movies.genre_id = genres.id
        WHERE genres.name = %s
    """
    cursor.execute(query, (genre_name,))
    movies = cursor.fetchall()
    cursor.close()
    conn.close()
    return movies
