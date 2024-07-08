import requests

URL = 'https://pokemonbattle.ru/v2'
TOKEN = '25d35ee8ceb779a99e65628aa76b73bb'
HEADER = {'Content-Type' : 'application/json'}
body_sozdanie = {
    "pokemon_id": "12331",
    "name": "Бишбармак",
    "photo_id": 2
}

response =  requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_sozdanie)

print(response)
