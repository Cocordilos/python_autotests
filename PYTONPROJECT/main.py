import requests

URL = 'https://pokemonbattle.ru/v2'
TOKEN = '25d35ee8ceb779a99e65628aa76b73bb'
HEADER = {'Content-Type' : 'application/json'}
body_sozdanie = {
    "trainer_token": TOKEN,
    "name": "Бомбазавр",
    "photo_id": 1
}

response =  requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_sozdanie)

print(response) 



