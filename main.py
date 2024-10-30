import requests


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a8d8fbc4607e1c2f5184946cf7ce67cf'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

TRAINER_NAME = "Кот Бегемот"
POKEMON_INITIAL_NAME = "Бульбазавр"
POKEMON_NEW_NAME = "java"
PHOTO_ID = 1

def make_request(method, endpoint, headers, body=None):
    '''Универсальная функция для отправки запросов HTTP.'''
    url = f'{URL}{endpoint}'
    if method == 'POST':
        return requests.post(url, headers=headers, json=body)
    elif method == 'PUT':
        return requests.put(url, headers=headers, json=body)
    raise ValueError("Unsupported HTTP method")

def print_response(response):
    '''Функция для печати JSON-ответа.'''
    print(response.json())

def main():
    # Регистрация тренера (если необходимо)
    body_registration = {
        "trainer_token": TOKEN,
        "email": "allochka.222@yandex.ru",
        "password": "222Makar222"
    }
    # response = make_request('POST', '/trainers/reg', HEADER, body_registration)
    # print_response(response)

    # Подтверждение email (если необходимо)
    body_confirmation = {"trainer_token": TOKEN}
    # response_confirmation = make_request('POST', '/trainers/confirm_email', HEADER, body_confirmation)
    # print_response(response_confirmation)
    
    # Создание покемона
    body_create = {"name": POKEMON_INITIAL_NAME, "photo_id": PHOTO_ID}
    response_create = make_request('POST', '/pokemons', HEADER, body_create)
    print_response(response_create)

    # Получение данных покемона
    pokemon_data = response_create.json()
    pokemon_id = pokemon_data.get('id')
    pokemon_name = pokemon_data.get('name', POKEMON_INITIAL_NAME)

    # Исходный вывод после создания
    print(f"Тренер: {TRAINER_NAME}, ID покемона: {pokemon_id}, Имя покемона: {pokemon_name}")

    # Изменение имени покемона
    body_update = {"pokemon_id": pokemon_id, "name": POKEMON_NEW_NAME, "photo_id": PHOTO_ID}
    response_update = make_request('PUT', '/pokemons', HEADER, body_update)
    print_response(response_update)

    # Вывод после изменения
    print(f"Тренер: {TRAINER_NAME}, ID покемона: {pokemon_id}, Новое имя покемона: {POKEMON_NEW_NAME}")

    # Поймать покемона в покебол
    body_add_pokeball = {"pokemon_id": pokemon_id}
    response_add_pokeball = make_request('POST', '/trainers/add_pokeball', HEADER, body_add_pokeball)
    print_response(response_add_pokeball)

if __name__ == "__main__":
    main()



   



   



   


