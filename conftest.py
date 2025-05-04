import pytest
import generators
import requests
import json
from curls import Url

@pytest.fixture
def create_courier():
    payload = generators.generate_courier_body()
    requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER_URL}', data = payload)
    payload_login = {'login': payload['login'],
                     'password': payload['password']}
    response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_URL}', data=payload_login)
    id_courier = response.json()['id']
    yield {
        'data_login': payload_login,
        'id': id_courier
    }
    requests.delete(f'{Url.BASE_URL}{Url.DELETE_COURIER_URL}{id_courier}')

@pytest.fixture()
def create_order():
    payload = generators.generate_data_order()
    payload_order = json.dumps(payload)
    response_track = requests.post(f'{Url.BASE_URL}{Url.CREATE_ORDER}', data = payload_order)
    track = response_track.json()
    response_id = requests.get(f'{Url.BASE_URL}{Url.GET_ID_ORDER}{track['track']}')
    id_order = response_id.json()
    return {
        'track_order': track,
        'id_order': id_order
    }

@pytest.fixture()
def return_id_order(create_order):
    track = create_order
    response = requests.get(f'{Url.BASE_URL}{Url.GET_ID_ORDER}{track['track']}')
    return response.json()