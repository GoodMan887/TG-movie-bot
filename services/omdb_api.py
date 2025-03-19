import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('OMDB_API_KEY')
IMDB_ID = 'tt0468569'

url = f'http://www.omdbapi.com/?i={IMDB_ID}&apikey={API_KEY}'
response = requests.get(url)
data = response.json()

title = data['Title']
description = data['Plot']
poster_url = data['Poster']

print(title)
print(description)
print(poster_url)
