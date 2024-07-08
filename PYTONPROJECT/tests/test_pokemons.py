import requests
import pytest

URL = 'https://pokemonbattle.ru/v2'
TOKEN = '25d35ee8ceb779a99e65628aa76b73bb'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '5976'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons/knockout', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200