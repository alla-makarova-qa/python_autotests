import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'aa8d8fbc4607e1c2f5184946cf7ce67cf'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '7316'


def test_status_code():
    response = requests.get(url=f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response.status_code == 200


def get_pokemon_id():
    response = requests.get(url=f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    response_data = response.json().get("data")
    if response_data and len(response_data) > 0:
        return response_data[0].get("id")
    return None


def test_part_of_response():
    response_get = requests.get(url=f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'java'

pokemon_id = get_pokemon_id()  # Получаем ID перед выполнением тестов

@pytest.mark.parametrize('key, value', [('name', 'java'), ('trainer_id', TRAINER_ID), ('id', pokemon_id)])


def test_parametrize(key, value):
    assert requests.get(url=f'{URL}/pokemons', params={'trainer_id': TRAINER_ID}).json()["data"][0][key] == value
    


