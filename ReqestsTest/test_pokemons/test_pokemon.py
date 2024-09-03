import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b8b578664ebb2fa1e4ac7cce1f65358a'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}
ID_TRAINER = '5450'

def test_valid_status_code():
    response_status = requests.get(f'{URL}/trainers', params = {'sort':'asc' })
    assert response_status.status_code == 200
    
def test_my_trainer_id():
    response_my_trainer_id = requests.get (f'{URL}/trainers', params = {'sort':'asc', 'trainer_id':ID_TRAINER } )
    assert response_my_trainer_id.json()['data'][0]["id"] == ID_TRAINER

