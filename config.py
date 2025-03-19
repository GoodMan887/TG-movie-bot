import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

print(BOT_TOKEN)

buttons = [
    'Боевик',
    'Фантастика',
    'Фэнтези',
    'Комедия',
    'Триллер',
    'Ужасы',
    'Криминал',
    'Драма',
    'Мелодрама',
]
