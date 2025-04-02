import os

import psycopg2


def connect_db():
    """Устанавливает подключение к БД."""
    return psycopg2.connect(
    dbname=os.getenv("DATABASE_NAME"),
    user=os.getenv("DATABASE_USER"),
    password=os.getenv("DATABASE_PASSWORD"),
    host=os.getenv("DATABASE_HOST"),
    port=os.getenv("DATABASE_PORT")
    )


def get_movies_by_genre(genre_name):
    """Возвращает список фильмов по заданному жанру."""
    conn = connect_db()
    cursor = conn.cursor()
    query = """
        SELECT title, genre, time, rating, year, description, poster_url
        FROM movies_v3
        WHERE genre ~* %s
    """
    cursor.execute(query, (rf'\y{genre_name}\y',))
    movies = cursor.fetchall()
    cursor.close()
    conn.close()
    return movies


def get_top_3_movies():
    """Возвращает 3 случайных фильма с рейтингом >= 7.0."""
    conn = connect_db()
    cursor = conn.cursor()
    query = """
            SELECT title, genre, time, rating, year, description, poster_url
            FROM movies_v3
            WHERE rating >= 7.0
            ORDER BY RANDOM()
            LIMIT 3
        """
    cursor.execute(query)
    movies = cursor.fetchall()
    cursor.close()
    conn.close()
    return movies


def get_random_movie():
    """Возвращает случайный фильм."""
    conn = connect_db()
    cursor = conn.cursor()
    query = """
    SELECT title, genre, time, rating, year, description, poster_url 
    FROM movies_v3
    ORDER BY RANDOM()
    LIMIT 1
    """
    cursor.execute(query)
    movie = cursor.fetchone()
    cursor.close()
    conn.close()
    return movie
