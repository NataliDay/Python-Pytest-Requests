import requests 

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'USER_TOKEN'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN }

body_registration = {
    "trainer_token": TOKEN,
    "email": "USER_LOGIN",
    "password": "USER_PASSWORD"
}

body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}
body_name ={
    "pokemon_id": "306800",
    "name": "OKI",
    "photo_id": 2
}
body_pokeball = {
    "pokemon_id": "306800"
}

'''response = requests.post(url = f'{URL}/trainers/reg/', headers = HEADER , json =body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER , json =body_confirmation)
print(response_confirmation.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER , json = body_create)
print(response_create.text)'''

'''message = response_create.json()['message']
print(message) '''

'''response_name = requests.put(url = f'{URL}/pokemons', headers = HEADER , json = body_name)
print(response_name.json())'''

'''response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER , json = body_pokeball)
print(response_pokeball.json())'''
