import requests
import pytest 

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'eb070ed3984945030061e1937d62f184'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN }
TRAINER_ID = '33467'

def test_status_code():
 response = requests.get(url = f'{URL}/trainers', params = {'level' : '5' },headers = HEADER)
 assert response.status_code == 200

def test_part_of_response():
 response_get = requests.get(url = f'{URL}/trainers' , params = {'trainer_id' : TRAINER_ID } , headers = HEADER)
 assert response_get.json()["data"][0]["id"] == '33467'

